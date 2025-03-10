import random as rnd
import time

target = input("請輸入顯示文字: ")

output = ""
for character in target:
    rand_char = chr(rnd.randint(32, 127))
    while rand_char != character:
        print(output+rand_char)
        rand_char = chr(rnd.randint(32, 127))
        time.sleep(0.01)
    output += character
    
    print(output)