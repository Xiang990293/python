#main.py
import os, warnings
from config import TICKERS, START_DATE, TEST_END
from data_loader import download_data
from features import engineer_features, prepare_data
from models import train_and_backtest
from visualization import plot_and_save_results
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Check for available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPUs detected: {len(gpus)}")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)  # Avoid full memory allocation
else:
    print("No GPU detected, running on CPU")

# 隱藏警告與設定不用 GPU (可依需求調整)
warnings.filterwarnings('ignore')
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# 主程式執行流程
def main():
    print("========================================")
    print("   AI 量化投資組合配置系統 (完美模組化版) ")
    print("========================================")
    
    # 1. 下載市場資料
    full_data, volume_data, vix_data = download_data(TICKERS, START_DATE, TEST_END)
    
    # 2. 生成量化特徵
    features = engineer_features(full_data, volume_data, vix_data, TICKERS)
    
    # 3. 準備神經網路輸入資料格式
    X_train, y_train, X_test, true_returns, dates, feat_names = prepare_data(features)
    
    # 4. 進行模型訓練與回測
    all_cums, all_weights, last_weight_hist = train_and_backtest(X_train, y_train, X_test, true_returns, feat_names)
    
    # 5. 繪製圖表並儲存結果
    plot_and_save_results(dates, all_cums, all_weights, true_returns, last_weight_hist, feat_names)
    print("✅ 程式執行完畢！")

if __name__ == "__main__":
    main()
