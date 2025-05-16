import os
import json

# 假設 valid_points 是從 JSON 解析並整理好的座標集合，例如：
# valid_points = set([(1,2), (3,4), (5,1), ...])
# 你的 JSON 解析程式碼應該類似：

# 讀取 JSON 檔案（假設每個列表是一組座標點）
with open('./minecraft_vanilla_server_home_grid/region_overworld.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # data 應該是一個列表，裡面包含多個座標點列表

valid_points = set()
for idx, (group, points) in enumerate(data.items()):
    # 將字串座標轉為整數
    x = []
    z = []
    for pt in points:
        x, z = map(int, pt.split(','))
        valid_points.add((x, z))

folder_path = '/mnt/sda1/FZSS/world/原味伺服器 - 最新版 - lite/world/poi'

for filename in os.listdir(folder_path):
    if filename.startswith('r.') and filename.endswith('.mca'):
        parts = filename.split('.')
        # 格式應該是 r.x.z.mca，長度4
        if len(parts) == 4:
            try:
                x = int(parts[1])
                z = int(parts[2])
                if (x, z) not in valid_points:
                    # 不在座標點清單，刪除檔案
                    file_path = os.path.join(folder_path, filename)
                    os.remove(file_path)
                    print(f"刪除檔案: {filename}")
            except ValueError:
                # 檔名中x,z無法轉成int，跳過
                continue
