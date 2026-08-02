"""
This is the brute force method, 
the old one with wrong answer got removed, 
check the old file preview instead if needed.
"""

n = int(input())
a = list(map(int, input().split(" ")))

total = sum(a)
minimum = None

def find_masum(b: int):
    vec = list(map(int,tuple(bin(b).replace("0b","").zfill(n))))
    
    return sum([vec[i] * a[i] for i in range(n)])

for i in range(2**n):
    sa = find_masum(i)
    sb = total - sa
    
    res = abs(sa - sb)
    if minimum is None:
        minimum = res
    elif minimum > res:
        minimum = res
     
    if minimum == 0:
        break
    


print(minimum)
