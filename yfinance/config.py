#config.py
# 基本設定與股票池
TICKERS = ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'KO', 'WMT', 'JPM', 'V', 'JNJ', 'XOM']
ALL_ASSETS = TICKERS + ['CASH'] 

# 回測時間範圍
START_DATE, END_DATE, TEST_END = '2015-01-01', '2024-01-01', '2026-01-01'

# 模型參數設定 (觀察期、執行次數、無風險利率)
LOOKBACK_PERIOD, NUM_RUNS, RF_DAILY = 60, 10, 0.04 / 252