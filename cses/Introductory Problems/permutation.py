import math
top: int = int(input(""))

con = None
if top == 1:
    print(1)
elif top < 3:
    print("NO SOLUTION")
elif top == 4:
    print("3 1 4 2")
else:
    diff = math.ceil(top/2)
    con = [(i, i+diff) for i in range(1, diff)]
        
    if top % 2 == 0:
        con.append((diff, top))
    else:
        con.append(diff)
    
    con = str(con)
    con = con.replace(")","").replace("(","").replace(", "," ").replace("]","").replace("[","")
        
    print(con)
