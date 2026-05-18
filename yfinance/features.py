#features.py
import pandas as pd
import numpy as np
# 🌟 核心修改：將 StandardScaler 替換為抗雜訊更強的 RobustScaler
from sklearn.preprocessing import RobustScaler
from config import RF_DAILY, END_DATE, LOOKBACK_PERIOD, ALL_ASSETS

# 計算 RSI 相對強弱指標
def compute_rsi(series, window=14):
    delta = series.diff()
    rs = delta.clip(lower=0).ewm(com=window-1, adjust=False).mean() / ((-1 * delta.clip(upper=0)).ewm(com=window-1, adjust=False).mean() + 1e-6)
    return 100 - (100 / (1 + rs))

# 核心特徵工程引擎
def engineer_features(full_data, volume_data, vix_data, tickers):
    print("🧠 正在計算量化特徵...")
    features = pd.DataFrame(index=full_data.index)
    
    # 計算 VIX 飆升乖離率
    vix_spike = (vix_data - vix_data.rolling(20).mean()) / (vix_data.rolling(20).mean() + 1e-6)

    # 針對每檔股票計算技術與量價特徵
    for t in tickers:
        ret, vol20 = full_data[t].pct_change(), volume_data[t]
        ma20, std20 = full_data[t].rolling(20).mean(), full_data[t].rolling(20).std()
        macd = full_data[t].ewm(span=12, adjust=False).mean() - full_data[t].ewm(span=26, adjust=False).mean()
        obv = (np.sign(full_data[t].diff()).fillna(0) * vol20).cumsum()

        features[f'{t}_Return'] = ret
        features[f'{t}_Vol'] = ret.rolling(20).std()
        features[f'{t}_RSI_14d'] = compute_rsi(full_data[t])
        features[f'{t}_Risk_Adj_Mom'] = (full_data[t] / full_data[t].shift(60) - 1) / (ret.rolling(60).std() * np.sqrt(252) + 1e-6)
        features[f'{t}_Vol_Ratio'] = vol20 / (vol20.rolling(20).mean() + 1e-6)
        features[f'{t}_Bias_60d'] = (full_data[t] - full_data[t].rolling(60).mean()) / (full_data[t].rolling(60).mean() + 1e-6)
        features[f'{t}_BB_PctB_20d'] = (full_data[t] - (ma20 - 2 * std20)) / (4 * std20 + 1e-6)
        features[f'{t}_5d_Return'] = full_data[t].pct_change(5)
        features[f'{t}_VIX_Spike'] = vix_spike
        features[f'{t}_MACD_Hist'] = (macd - macd.ewm(span=9, adjust=False).mean()) / (full_data[t] + 1e-6)
        features[f'{t}_Drawdown_60d'] = (full_data[t] - full_data[t].rolling(60, min_periods=1).max()) / (full_data[t].rolling(60, min_periods=1).max() + 1e-6)
        features[f'{t}_OBV_Bias'] = (obv - obv.rolling(20).mean()) / (obv.rolling(20).mean().abs() + 1e-6)

    # 計算橫截面特徵 (所有股票 RSI 的 Z-score)
    rsi_cols = [f'{t}_RSI_14d' for t in tickers]
    rsi_mean, rsi_std = features[rsi_cols].mean(axis=1), features[rsi_cols].std(axis=1) + 1e-6
    for t in tickers: features[f'{t}_RSI_Z'] = (features[f'{t}_RSI_14d'] - rsi_mean) / rsi_std

    # 強制補齊 CASH (現金) 部位的預設特徵值
    cash_defaults = {'Return': RF_DAILY, 'Vol': 1e-6, 'RSI_14d': 50.0, 'Risk_Adj_Mom': 0.0, 'Vol_Ratio': 1.0, 'RSI_Z': 0.0, 'Bias_60d': 0.0, 'BB_PctB_20d': 0.5, '5d_Return': RF_DAILY * 5, 'VIX_Spike': 0.0, 'MACD_Hist': 0.0, 'Drawdown_60d': 0.0, 'OBV_Bias': 0.0}
    for k, v in cash_defaults.items(): features[f'CASH_{k}'] = v

    return features.dropna()

# 製作給 LSTM 使用的 3D 滑動視窗 (Samples, Timesteps, Features)
def create_sliding_windows(scaled_df, raw_df, lookback):
    X = [scaled_df.iloc[i-lookback:i].values for i in range(lookback, len(scaled_df))]
    y = [raw_df[[f'{a}_Return' for a in ALL_ASSETS]].iloc[i].values for i in range(lookback, len(raw_df))]
    return np.array(X), np.array(y)

# 資料預處理 (切分訓練與測試集、強健縮放)
def prepare_data(features):
    tr, te = features[:END_DATE], features[END_DATE:]
    
    # 🌟 核心修改：改用 RobustScaler 來過濾金融市場的極端黑天鵝雜訊
    scaler = RobustScaler()
    
    # 進行特徵縮放
    tr_sc = pd.DataFrame(scaler.fit_transform(tr), index=tr.index, columns=tr.columns)
    te_sc = pd.DataFrame(scaler.transform(te), index=te.index, columns=te.columns)
    
    # 生成訓練與測試的張量
    X_train, y_train = create_sliding_windows(tr_sc, tr, LOOKBACK_PERIOD)
    X_test, y_test = create_sliding_windows(te_sc, te, LOOKBACK_PERIOD)
    
    return X_train, y_train, X_test, y_test, te.index[LOOKBACK_PERIOD:], features.columns.tolist()
