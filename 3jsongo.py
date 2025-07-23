import json

with open("inventory_data.json", "r", encoding="utf-8") as all_item:
    all_item = json.load(all_item)["Items"]
    with open("zh-tw.json", "r", encoding="utf-8") as trans:
        trans = json.load(trans)
        with open("output.json", "w", encoding="utf-8") as output:
            temp = dict()
            for item in all_item:
                try:
                    print(item["item"], trans[item["item"]])
                    temp[item["item"]] = trans[item["item"]]
                except:
                    pass
                
            output.write(json.dumps(temp, ensure_ascii=False))