n = int(input())

dp = []

def dp_solver(a: int, b: int):
    try:
        if dp[a][b]:
            return dp[a][b]
        
        if dp[b][a]:
            return dp[b][a]
    except:
        if a < b:
            a, b = b, a
            
        diff = a - b
        if diff > b:
            return False
            
        if (b - diff) % 3 != 0:
            return False
            
        return True
    
    
for _ in range(n):
    a, b = map(int, input().split(" "))
    
    print("YES" if dp_solver(a, b) else "NO")
