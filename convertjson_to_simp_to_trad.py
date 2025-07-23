import json
import os
from opencc import OpenCC

converter = OpenCC('s2t')


def merge_data(correct_data, comparison_data):
    for key, value in correct_data.items():
        if isinstance(value, dict):
            comparison_data[key] = {}
            merge_data(value, comparison_data[key])
        elif key not in comparison_data:
            print(type(value))
            
            comparison_data[key] = converter.convert(value)
            print(value, converter.convert(value))


with open("/usr/local/bin/Mine-imator/Data/Languages/chinese(Traditional).milanguage", "w", encoding="utf-8") as output:
    with open("/usr/local/bin/Mine-imator/Data/Languages/chinese(Traditional)data.milanguage", "r", encoding="utf-8") as tw:
        with open("/home/xiang990293/下載/chinese.milanguage", "r", encoding="utf-8") as cn:
            tw_data = json.load(tw)
            cn_data = json.load(cn)
            temp = []
            
            
            # Find missing keys in comparison file
            merge_data(cn_data, tw_data)

            # Write the updated comparison file to a new output file
            # json.dump(tw_data, output, indent=4)
            output.write(json.dumps(tw_data, ensure_ascii=False, indent=4))