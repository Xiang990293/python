source = input()

static = {}
middle = 0
mid_c = ""
while source != "":
    ch = source[0]
    for c in source:
        if c == ch:
            if ch not in static.keys():
                static[ch] = 1
            else:
                static[ch] += 1
            
    if static[ch] % 2 == 1:
        middle += 1
        mid_c = ch
        
    if middle > 1:
        break
            
    source = source.replace(ch, "")

result = ""
   
if middle > 1:
    print("NO SOLUTION")
elif middle == 1:
    result = mid_c

for k in static.keys():
    if k == mid_c:
        continue
    
    while static[k] > 0:
        result = f"{k}{result}{k}"
        static[k] -= 2
        
print(result)
