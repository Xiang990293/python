n = int(input())

def res(n):
    return int(0.5*n**4-4.5*n**2+12*n-8)
    
    
for i in range(1,n+1):
    print(res(i))
