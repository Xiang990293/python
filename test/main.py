from PIL import Image, ImageEnhance
import numpy as np

# 讀取圖片
grass_top = Image.open("./test/grass_top.png").convert("RGBA")
test_texture = Image.open("./test/test_texture.png").convert("RGBA")

# 目標尺寸
target_size = (64, 64)

# 從 test_texture 擷取右上角顏色（假設分成 4 等寬區塊，右上是第3塊）
w, h = test_texture.size
block_w = w // 4
target_block = test_texture.crop((0, block_w, block_w, block_w*2))

# 計算目標方塊平均色
target_avg = np.array(target_block).mean(axis=(0, 1))

# 將 grass_top 調整到 64x64
grass_resized = grass_top.resize(target_size, Image.NEAREST)

# 計算 grass_top 平均色
grass_avg = np.array(grass_resized).mean(axis=(0, 1))

# # 計算顏色比例調整因子（避免 alpha 通道）
# scale_factors = target_avg[:3] / np.maximum(grass_avg[:3], 1)

# 對 RGB 通道進行縮放
grass_array = np.array(grass_resized, dtype=np.float32)
# print(scale_factors)
grass_array[:, :, 0] = np.clip(grass_array[:, :, 0] * 0.8, 0, 255)
grass_array[:, :, 1] = np.clip(grass_array[:, :, 1] * 1.3, 0, 255)
grass_array[:, :, 2] = np.clip(grass_array[:, :, 2] * 0.6, 0, 255)

# 保存結果
grass_matched = Image.fromarray(grass_array.astype(np.uint8), mode="RGBA")
output_path = "./test/grass_top_color_matched.png"
grass_matched.save(output_path)

output_path
