import os

with open("testing_all_item.txt", "r", encoding="utf-8") as input:
    input = input.read()
    input = input.split("\n")
    for i in input:
        print(f"summon item ~ ~-5 ~ {"{"}Item:{"{"}id:{str(i).lower()}{'}}'}")