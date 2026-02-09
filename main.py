import json

# def main():
#     print("Hello from python!")


# if __name__ == "__main__":
#     main()

with open("/home/xiang990293/curseforge/minecraft/Instances/SkyFactory 4 (1)/config/prestige/rewards.json") as tw:
    with open("/home/xiang990293/curseforge/minecraft/Instances/SkyFactory 4 (1)/config/prestige/backup/rewards.json") as en:
        trans_data = json.load(tw)
        original_data = json.load(en)
        
        diff_tw_from_en = set()
        for item in trans_data:
            diff_tw_from_en.add(item['identifier'])
            for i in original_data:
                if item['identifier'] == i['identifier']:
                    diff_tw_from_en.remove(i['identifier'])
                    continue        
                
        diff_en_from_tw = set()
        for item in original_data:
            diff_en_from_tw.add(item['identifier'])
            for i in trans_data:
                if item['identifier'] == i['identifier']:
                    diff_en_from_tw.remove(i['identifier'])
                    continue
        
        diff_tw_from_en.union(diff_en_from_tw)
        print(diff_tw_from_en)
                
                    
        # json.dump(trans_data, open("/home/xiang990293/curseforge/minecraft/Instances/SkyFactory 4 (1)/resourcepacks/SkyFactory 4中文化檔/config/prestige/rewards.json", "w"))