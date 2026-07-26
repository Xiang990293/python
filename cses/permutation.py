import math
top: int = int(input(""))

con: str = ""
if top == 1:
    print(1)
elif top < 3:
    print("NO SOLUTION")
elif top == 4:
    print("3 1 4 2")
else:
    diff = math.ceil(top/2)
    for i in range(1, diff):
        con += f"{str(i)} {str(i+diff)} "
        
    if top % 2 == 0:
        con += f"{diff} {top}"
    else:
        con += f"{diff}"
        
print(con)