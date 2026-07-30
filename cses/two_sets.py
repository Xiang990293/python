n = int(input())

def formatified(l: list) -> (int, str):
    return str(l).replace("[","").replace("]","").replace("(","").replace(")","").replace(", "," ")

if n % 4 == 0:
    print("YES")
    print(n//2)
    print(f"{formatified(list(range(1,n//4+1)))} {formatified(list(range(3*n//4+1, n+1)))}")
    print(n//2)
    print(formatified(list(range(n//4+1, 3*n//4+1))))
    
elif n % 4 == 3:
    print("YES")
    print((n+1)//2)
    print(f"{formatified(list(range(1,(n+1)//4+1)))} {formatified(list(range(3*(n+1)//4+1, n+1)))} {(n+1)//2}")
    print((n+1)//2-1)
    mid = list(range((n+1)//4+1, 3*(n+1)//4+1))
    mid.remove((n+1)//2)
    print(formatified(mid))
    
else:
    print("NO")
