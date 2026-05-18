#visualization.py
import os, matplotlib.pyplot as plt, seaborn as sns, numpy as np
from datetime import datetime
from config import TICKERS, ALL_ASSETS

# 繪製回測結果與 AI 特徵決策圖表
def plot_and_save_results(dates, all_ai_cums, all_ai_weights, true_returns, last_weight_history, feature_names):
    print("\n📊 正在生成 3 張分析圖表...")
    
    # 計算 AI 平均表現與等權重(Baseline)表現
    mean_ai_cum, mean_ai_weights = np.mean(all_ai_cums, axis=0), np.mean(all_ai_weights, axis=0)
    eq_cum = (1 + np.mean(true_returns[:, :len(TICKERS)], axis=1)).cumprod()

    # --- 圖 1：績效對比與資產配置 ---
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # 繪製各次執行的細線與平均粗線
    for i, cum in enumerate(all_ai_cums): ax1.plot(dates, cum, color='crimson', alpha=0.15, lw=1, label='Individual AI Runs' if i==0 else "")
    ax1.plot(dates, mean_ai_cum, label='AI Average', color='red', lw=3)
    ax1.plot(dates, eq_cum, label='Equal Weight', color='black', ls='--', lw=2)
    
    # 標示最終淨值
    ax1.text(dates[0], max(mean_ai_cum.max(), eq_cum.max()) * 0.9, f'Avg AI: {mean_ai_cum[-1]:.3f}\nBaseline: {eq_cum[-1]:.3f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
    ax1.set(title='Backtesting Result: AI vs Equal Weight', ylabel='Cumulative Return')
    ax1.legend(loc='upper left'); ax1.grid(True, alpha=0.3)

    # 繪製股債(現金)比例堆疊圖
    ax2.stackplot(dates, np.sum(mean_ai_weights[:, :len(TICKERS)], axis=1)*100, mean_ai_weights[:, -1]*100, labels=['Equity (%)', 'Cash (%)'], colors=['#ff9999', '#aed6f1'])
    ax2.set(title='Asset Allocation', ylabel='Weight (%)'); ax2.legend(loc='upper right')
    fig1.tight_layout()

    # --- 圖 2：資金權重熱力圖 ---
    fig2, ax_heat = plt.subplots(figsize=(14, 8))
    sns.heatmap(mean_ai_weights.T, cmap='YlGnBu', ax=ax_heat, xticklabels=50)
    ax_heat.set(yticklabels=ALL_ASSETS, title="Average Portfolio Heatmap", xlabel="Trading Days", ylabel="Assets")
    plt.setp(ax_heat.get_yticklabels(), rotation=0); fig2.tight_layout()

    # --- 圖 3：XAI 模型特徵重要性變化 ---
    fig3, ax_xai = plt.subplots(figsize=(14, 8))
    core_features = {'Return': 'Daily Return', 'Vol': '20d Volatility', 'RSI_14d': 'RSI 14d', 'Risk_Adj_Mom': 'Risk-Adj Momentum', 'Vol_Ratio': 'Volume Ratio', 'RSI_Z': 'RSI Z', 'Bias_60d': '60d Bias', 'BB_PctB_20d': 'Bollinger %B', 'MACD_Hist': 'MACD Hist', 'OBV_Bias': 'OBV Bias', '5d_Return': '5d Return', 'VIX_Spike': 'VIX Spike'}
    feature_history_arr = np.array(last_weight_history) 
    
    # 抓取各核心特徵對應的索引並繪製折線圖
    for key, label in core_features.items():
        indices = [j for j, name in enumerate(feature_names) if key in name]
        if indices: ax_xai.plot(np.mean(feature_history_arr[:, indices], axis=1), label=label, lw=2)

    ax_xai.set(title="XAI: Core Feature Importance", xlabel="Epochs", ylabel="Mean Absolute Weight Magnitude")
    ax_xai.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10); ax_xai.grid(True, alpha=0.5)
    fig3.tight_layout()

    # --- 建立資料夾並存檔 ---
    save_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "new"))
    os.makedirs(save_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    for fig, name in zip([fig1, fig2, fig3], ['1_Performance', '2_Allocation_Heatmap', '3_Feature_XAI']):
        fig.savefig(os.path.join(save_dir, f"{name}_{ts}.png"), dpi=300, bbox_inches='tight' if 'XAI' in name else None)

    print(f"📁 3 張圖表已精準儲存至: {save_dir}")
