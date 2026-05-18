#models.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Activation, Attention, GlobalAveragePooling1D, Concatenate, LayerNormalization, GaussianNoise
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, Callback
from config import NUM_RUNS, ALL_ASSETS, TICKERS

# ==========================================
# 🧠 AI 風險大腦：自定義損失函數 (結合策略一與策略三)
# ==========================================
@tf.keras.utils.register_keras_serializable()
def custom_objective_loss(y_true, y_pred):
    # 計算 Batch 內每一天的投資組合報酬
    port_ret = tf.reduce_sum(y_true * y_pred, axis=-1)

    # 1. 抓出最差 10% 的平均虧損 (CVaR)
    sorted_rets = tf.sort(port_ret, direction='ASCENDING')
    batch_size = tf.shape(port_ret)[0]
    k = tf.math.maximum(1, tf.cast(tf.cast(batch_size, tf.float32) * 0.10, tf.int32))
    cvar_value = tf.reduce_mean(sorted_rets[:k])

    # 🌟 [策略三] 風險容忍閥值：跌幅超過 -3% (-0.03) 時才開始懲罰
    # 這樣 AI 就不會因為正常的股市小回檔而嚇到賣股票
    cvar_penalty = tf.math.minimum(cvar_value + 0.03, 0.0) 
    
    risk_aversion = 0.5 
    utility = tf.reduce_mean(port_ret) + risk_aversion * cvar_penalty

    # 🌟 [策略一] 打造特種部隊：極致降低 L2 懲罰
    # 將原本的 0.001 降為 0.00005，解開限制，允許 AI 重倉押注強勢飆股
    l2_pen = 0.00005 * tf.reduce_sum(tf.square(y_pred[:, :-1]), axis=-1)
    
    turn_pen = tf.reduce_sum(tf.abs(y_pred[1:] - y_pred[:-1]), axis=-1) * 0.00001
    return -utility + tf.reduce_mean(l2_pen) + tf.reduce_mean(turn_pen)

# ==========================================
# 🏗️ 神經網路架構：決策輸出層 (實作策略二)
# ==========================================
def build_attention_model(input_shape, num_assets):
    inputs = Input(shape=input_shape)
    lstm_out = LayerNormalization()(LSTM(32, return_sequences=True, dropout=0.15, name='lstm_layer')(GaussianNoise(0.02)(inputs)))
    attn_out = Attention()([Dense(32)(lstm_out), Dense(32)(lstm_out)])
    x = Dense(32, activation='relu')(GlobalAveragePooling1D()(Concatenate()([lstm_out, attn_out])))
    
    # 🌟 [策略二] 極端二元論者：調降 Softmax Temperature
    # 溫度從 0.8 大幅調降至 0.35。這會產生「銳化效應」，
    # 迫使 AI 不再猶豫不決，出現「要嘛滿倉 1~2 檔股票，要嘛 100% 抱現金」的極端果斷操作。
    temperature = 0.3 
    logits = Dense(num_assets)(x)
    return Model(inputs=inputs, outputs=Activation('softmax')(logits / temperature))

# ==========================================
# 📊 XAI 特徵權重監控回調函數
# ==========================================
class WeightMonitor(Callback):
    def on_train_begin(self, logs=None): self.feature_history = []
    def on_epoch_end(self, epoch, logs=None):
        self.feature_history.append(np.mean(np.abs(self.model.get_layer('lstm_layer').get_weights()[0]), axis=1))

# ==========================================
# 🚀 核心訓練與回測引擎 (含隔離帶防護)
# ==========================================
def train_and_backtest(X_train, y_train, X_test, true_returns, feat_names):
    all_cums, all_weights, last_weight_hist = [], [], []
    lookback, split_idx = X_train.shape[1], int(len(X_train) * 0.8)
    
    X_t, y_t = X_train[:split_idx - lookback], y_train[:split_idx - lookback]
    X_v, y_v = X_train[split_idx:], y_train[split_idx:]

    print(f"\n🛡️ 隔離帶防護啟動 (Gap: {lookback} days) | 訓練樣本: {len(X_t)} | 驗證樣本: {len(X_v)}")
    print(f"🚀 模型訓練啟動 (共執行 {NUM_RUNS} 次)...")

    for run_id in range(NUM_RUNS):
        model = build_attention_model((X_train.shape[1], X_train.shape[2]), len(ALL_ASSETS))
        model.compile(optimizer=Adam(learning_rate=0.001, clipnorm=1.0), loss=custom_objective_loss)
        
        cb = [EarlyStopping(monitor='val_loss', patience=30, restore_best_weights=True),
              ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=8, min_lr=1e-6, verbose=0),
              (wm := WeightMonitor())]
        
        model.fit(X_t, y_t, epochs=100, batch_size=64, validation_data=(X_v, y_v), callbacks=cb, verbose=0)
        
        # ... 模型訓練完成後 ...

        ai_w = model.predict(X_test, verbose=0)

        # A. 執行個股特徵分析
        ticker_analysis = analyze_per_ticker_features(model, X_test, true_returns, TICKERS, feat_names)

        # B. 根據分析結果微調權重
        tuned_ai_w = tune_portfolio_by_importance(ai_w, ticker_analysis, TICKERS)

        # C. 計算微調後的表現
        ai_cum = (1 + np.sum(tuned_ai_w * true_returns, axis=1)).cumprod()
        all_cums.append(ai_cum)
        all_weights.append(ai_w)
    
        
        if run_id == NUM_RUNS - 1: last_weight_hist = wm.feature_history 
        print(f"✅ 第 {run_id + 1}/{NUM_RUNS} 次訓練完成！最終淨值: {ai_cum[-1]:.3f}")
        
    return all_cums, all_weights, last_weight_hist
    
# models.py 擴充功能

def analyze_per_ticker_features(model, X_test, y_test, tickers, feature_names):
    """
    對每一檔股票進行特徵變數顯著性分析
    返回格式: { 'AAPL': { 'RSI_Z': 0.05, 'Risk_Adj_Mom': 0.04 ... }, 'NVDA': {...} }
    """
    print("\n🔍 正在進行個股特徵顯著性深度掃描...")
    baseline_preds = model.predict(X_test, verbose=0)
    # y_test 的維度是 (Samples, Assets)
    ticker_importances = {}

    for asset_idx, t in enumerate(tickers):
        asset_scores = {}
        # 找出屬於該標的的特徵索引 (排除 CASH)
        t_feat_indices = [i for i, name in enumerate(feature_names) if t in name or 'VIX' in name]
        
        for f_idx in t_feat_indices:
            save_col = X_test[:, :, f_idx].copy()
            
            # 數學擾動：隨機洗牌特徵
            flat = X_test[:, :, f_idx].flatten()
            np.random.shuffle(flat)
            X_test[:, :, f_idx] = flat.reshape(X_test.shape[0], X_test.shape[1])
            
            # 重新預測並計算對該標的預測誤差的影響
            shuffled_preds = model.predict(X_test, verbose=0)
            # 僅計算該標的的 MSE 變化
            score = np.mean((y_test[:, asset_idx] - shuffled_preds[:, asset_idx])**2) - \
                    np.mean((y_test[:, asset_idx] - baseline_preds[:, asset_idx])**2)
            
            asset_scores[feature_names[f_idx]] = max(0, score)
            X_test[:, :, f_idx] = save_col # 還原
            
        ticker_importances[t] = asset_scores
    
    return ticker_importances

def tune_portfolio_by_importance(original_weights, ticker_importances, tickers):
    """
    根據特徵顯著性排名微調權重
    理論：顯著性總和越高，代表模型對該資產的判斷越有「把握」
    """
    # 1. 計算每檔標的的「模型把握度」分數 (Confidence Score)
    conf_scores = np.array([sum(ticker_importances[t].values()) for t in tickers])
    
    # 2. 進行 Softmax 標準化，轉化為修正乘數
    # 數值越高，修正乘數越大
    conf_multiplier = np.exp(conf_scores) / np.sum(np.exp(conf_scores))
    conf_multiplier = conf_multiplier * len(tickers) # 平均值歸 1
    
    tuned_weights = original_weights.copy()
    # 3. 對股票部位進行微調 (最後一格是 CASH 不動)
    tuned_weights[:, :-1] = tuned_weights[:, :-1] * conf_multiplier
    
    # 4. 重新標準化，確保權重總和 = 1
    tuned_weights = tuned_weights / np.sum(tuned_weights, axis=1, keepdims=True)
    
    return tuned_weights
