import json
import os

with open("/mnt/sda1/coding project/resource-pack-for-rippou-ripple-survival-server/assets/template/models/item/output.json", "w", encoding="utf-8") as output:
    with open("dark_maroon_splashes.json", "r", encoding="utf-8") as input_file:
        input_data = json.load(input_file)["nbt"][0]["value"][2]["value"]["list"]
        temp = []
        
        for block in input_data:
            if block[1]["value"] not in [0, 1, 2, 4, 5, 6]:
                continue
            
            temp.append({
                "from": block[0]["value"]["list"],
                "to": [i+1 for i in block[0]["value"]["list"]],
                "faces": {
                    "north": {"uv": [0, 0, 2, 2], "texture": "#missing"},
                    "east": {"uv": [0, 0, 2, 2], "texture": "#missing"},
                    "south": {"uv": [0, 0, 2, 2], "texture": "#missing"},
                    "west": {"uv": [0, 0, 2, 2], "texture": "#missing"},
                    "up": {"uv": [0, 0, 2, 2], "texture": "#missing"},
                    "down": {"uv": [0, 0, 2, 2], "texture": "#missing"}
                },
                "color": block[1]["value"]
            })

        output.write(json.dumps({"format_version":"1.21.6", "elements": temp}, ensure_ascii=False))