import os
import json

node_set = set()
path_set = set()

item_to_tag = dict()

def set_item_tag_map(item, tag):
    if item in item_to_tag:
        if type(item_to_tag[item]) != str:
            tag += item_to_tag[item]
            return
        else:
            tag = [item_to_tag[item]] + [tag]
            return
    
    item_to_tag[item] = tag
    return

def parse_tag(item):
    if "#" in item:
        try:
            items = json.load(open(f"./minecraft crafting path/block_tag/{item[11:]}.json"))["values"]
            for i in items:
                set_item_tag_map(i, item)
            return items
        except FileNotFoundError:
            return item
    
    if type(item) != str and type(item) != list:
        TypeError("what the hack is this?", item)
        return ""
    return item

for recipe in os.listdir("./minecraft crafting path/recipe"):
    with open(f"./minecraft crafting path/recipe/{recipe}", "r") as f:
        content = json.load(f)
        recipe_type = content["type"]
        if recipe_type == "minecraft:crafting_shaped":
            ingredients_items = []
            for items in content["key"].values():
                if type(items) == str:
                    ingredients_items.append(items)
                elif type(items) == list:
                    ingredients_items.extend(items)
                else:
                    continue
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
            
            pass
        elif recipe_type == "minecraft:crafting_shapeless":
            ingredients_items = content["ingredients"]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:smelting":
            ingredients_items = parse_tag(content["ingredient"])
            if type(ingredients_items) == list:
                pass
            else:
                ingredients_items = [ingredients_items]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    continue
                    
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:smoking":
            ingredients_items = parse_tag(content["ingredient"])
            if type(ingredients_items) == list:
                pass
            else:
                ingredients_items = [ingredients_items]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:campfire_cooking":
            ingredients_items = parse_tag(content["ingredient"])
            if type(ingredients_items) == list:
                pass
            else:
                ingredients_items = [ingredients_items]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:stonecutting":
            ingredients_items = parse_tag(content["ingredient"])
            if type(ingredients_items) == list:
                pass
            else:
                ingredients_items = [ingredients_items]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:blasting":
            ingredients_items = parse_tag(content["ingredient"])
            if type(ingredients_items) == list:
                pass
            else:
                ingredients_items = [ingredients_items]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif recipe_type == "minecraft:smithing_transform":
            ingredients_items = [content["addition"]] + [content["base"]]
            result_item = content["result"]["id"]
            
            node_set.add({
                "id": result_item.replace("minecraft:", ""),
                "name": result_item.replace("minecraft:", "").replace("_", " "),
            }.__str__())
            
            while ingredients_items != []:
                ingredient = parse_tag(ingredients_items.pop(0))
                if type(ingredient) == list:
                    for i in ingredient:
                        ingredients_items.append(i)
                    continue
                
                node_set.add({
                    "id": ingredient.replace("minecraft:", ""),
                    "name": ingredient.replace("minecraft:", "").replace("_", " "),
                }.__str__())
            
                path_set.add({
                    "type": recipe_type,
                    "startNodeId": ingredient.replace("minecraft:", ""),
                    "endNodeId": result_item.replace("minecraft:", "")
                }.__str__())
                
            pass
        elif content["type"] in [
            "minecraft:smithing_trim",
            "minecraft:crafting_special_repairitem",
            "minecraft:crafting_special_bannerduplicate",
            "minecraft:crafting_special_bookcloning",
            "minecraft:crafting_special_mapcloning",
            "minecraft:crafting_special_mapextending",
            "minecraft:crafting_special_firework_star_fade",
            "minecraft:crafting_special_firework_rocket",
            "minecraft:crafting_special_firework_star",
            "minecraft:crafting_special_armordye",
            "minecraft:crafting_special_shielddecoration",
            "minecraft:crafting_special_tippedarrow",
            "minecraft:crafting_transmute",
            "minecraft:crafting_decorated_pot"
        ]:
            pass
        else:
            # print(content["type"], content)
            pass

    
SUSPICIOUS_SAND = {
    "desert_well.json": "suspicious_sand",
    "trail_ruins_rare.json": "suspicious_sand",
    "trail_ruins_common.json": "suspicious_sand",
    "ocean_ruin_warm.json": "suspicious_gravel",
    "ocean_ruin_cold.json": "suspicious_gravel"
}
node_set.add({
    "id": "suspicious_sand",
    "name": "suspicious sand",
}.__str__())
node_set.add({
    "id": "suspicious_gravel",
    "name": "suspicious gravel",
}.__str__())
node_set.add({
    "id": "sheep",
    "name": "sheep",
}.__str__())


for loot_table in os.listdir("./minecraft crafting path/loot_table"):
    with open(f"./minecraft crafting path/loot_table/{loot_table}", "r") as f:
        loot = json.load(f)
        
        loot_type = loot["type"]
        
        if loot_type == "minecraft:entity":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:block":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                # print(alternative)
                                pass
                    else:
                        # print(entry)
                        pass
            pass
        elif loot_type == "minecraft:chest":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                # print(alternative)
                                pass
                    else:
                        # print(entry)
                        pass
            pass
        elif loot_type == "minecraft:shearing":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": "sheep",
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:gift":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": "villager_"+loot_table,
                "name": "villager "+loot_table.replace("_gift.json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": "villager_"+loot_table,
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": "villager_"+loot_table,
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:archaeology":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": SUSPICIOUS_SAND[loot_table],
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": alternative["type"],
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:fishing":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:equipment":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        elif loot_type == "minecraft:barter":
            if "pools" not in loot.keys():
                continue
            
            pools = loot["pools"]
            node_set.add({
                "id": loot_table.replace(".json", ""),
                "name": loot_table.replace(".json", "").replace("_", " "),
            }.__str__())
            for pool in pools:
                pool_entries = pool["entries"]
                for entry in pool_entries:
                    if entry["type"] == "minecraft:item":
                        item = parse_tag(entry["name"])
                        if type(item) == list:
                            for i in item:
                                item.append(i)
                            continue
                        else:
                            item = [item]
                        
                        for i in item:
                            node_set.add({
                                "id": i.replace("minecraft:", ""),
                                "name": i.replace("minecraft:", "").replace("_", " "),
                            }.__str__())
                            
                            path_set.add({
                                "type": loot_type,
                                "startNodeId": loot_table.replace(".json", ""),
                                "endNodeId": i.replace("minecraft:", "")
                            }.__str__())
                    elif entry["type"] == "minecraft:loot_table":
                        pass
                    elif entry["type"] == "minecraft:alternatives":
                        for alternative in entry["children"]:
                            if alternative["type"] == "minecraft:item":
                                item = parse_tag(alternative["name"])
                                if type(item) == list:
                                    for i in item:
                                        item.append(i)
                                    continue
                                else:
                                    item = [item]
                                
                                for i in item:
                                    node_set.add({
                                        "id": i.replace("minecraft:", ""),
                                        "name": i.replace("minecraft:", "").replace("_", " "),
                                    }.__str__())
                                    
                                    path_set.add({
                                        "type": loot_type,
                                        "startNodeId": loot_table.replace(".json", ""),
                                        "endNodeId": i.replace("minecraft:", "")
                                    }.__str__())
                            elif alternative["type"] == "minecraft:loot_table":
                                pass
                            else:
                                pass
                    else:
                        pass
            pass
        else:
            pass



output = json.dumps({"nodes":[eval(_) for _ in node_set], "paths":[eval(_) for _ in path_set]})
print(output)
