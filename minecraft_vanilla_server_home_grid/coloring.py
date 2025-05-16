import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


plt.rcParams["font.sans-serif"] = ["SimHei"]  # 設定黑體字，Windows常見中文字體
plt.rcParams["axes.unicode_minus"] = False   # 解決負號顯示問題

# 讀取 JSON 檔案（假設每個列表是一組座標點）
with open('./minecraft_vanilla_server_home_grid/region_overworld.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # data 應該是一個列表，裡面包含多個座標點列表

# 取 15 種顏色，可以用 Tableau Palette 或自訂
tableau_colors = list(mcolors.TABLEAU_COLORS.keys())
# 若不足15，可加上自訂顏色
custom_colors = tableau_colors + [
    '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
    '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
    '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000'
]
color_list = custom_colors[:15]  # 取前15種

plt.figure(figsize=(12, 10))

for idx, (group, points) in enumerate(data.items()):
    # 將字串座標轉為整數
    x = []
    y = []
    for pt in points:
        px, py = map(int, pt.split(','))
        x.append(512*px)
        y.append(512*py)
    plt.scatter(x, y, color=color_list[idx % len(color_list)], label=group, s=100, marker='.',linewidths=0.5)

plt.legend(fontsize=10, loc='best')
plt.title('各分類座標點分色圖')
plt.xlabel('X')
plt.ylabel('Z')
plt.grid(True)
plt.savefig('colored_groups.png')
plt.show()
