t = int(input())

def solver(n, a, b)->(bool, str, str):
    if n == 0:
        return True, "", ""
    
    if n < a + b:
        return False, "", ""
    
    if a >= n or b >= n:
        return False, "", ""
    
    if n > a + b:
        sol, resa, resb = solver(a+b, a, b)
        
        for i in range(a+b+1, n+1):
            resa += f"{i} "
            resb += f"{i} "
        return sol, resa, resb
        
        
    resa = ""
    resb = ""
    for i in range(a):
        resa += f"{i+b+1} "
        resb += f"{i+1} "
        
    for i in range(a+1, n+1):
        resa += f"{i-a} "
        resb += f"{i} "
        
    return True, resa, resb
        
    

for i in range(t):
    n, a, b = map(int, input().split(" "))
    
    res, resa, resb = solver(n, a, b)
    
    if not res:
        print("NO")
        continue
        
    print("YES")
    print(resa)
    print(resb)
    
