#data_loader.py
import yfinance as yf
import pandas as pd

# 從 Yahoo Finance 下載股票與 VIX 歷史資料
def download_data(tickers, start, end):
    print(f"📥 正在下載 {len(tickers)} 檔個股與 VIX 恐慌指數資料...")
    full_data, volume_data = pd.DataFrame(), pd.DataFrame()

    # 迴圈下載各股收盤價與成交量
    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end, progress=False)
        if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
        full_data[ticker] = df['Adj Close'] if 'Adj Close' in df.columns else df['Close']
        volume_data[ticker] = df['Volume']
        
    # 下載 VIX 恐慌指數作為宏觀避險特徵
    vix_df = yf.download('^VIX', start=start, end=end, progress=False)
    if isinstance(vix_df.columns, pd.MultiIndex): vix_df.columns = vix_df.columns.get_level_values(0)
    vix_data = vix_df['Adj Close'] if 'Adj Close' in vix_df.columns else vix_df['Close']

    # 回傳填補缺失值後的資料
    return full_data.ffill().dropna(), volume_data.ffill().dropna(), vix_data.ffill().dropna()