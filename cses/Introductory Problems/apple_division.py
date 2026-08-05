"""
This is the brute force method, 
the old one with wrong answer got removed, 
check the old file preview instead if needed.
"""

n = int(input())
a = list(map(int, input().split(" ")))

total = sum(a)

def solver(l, minimum, ps = 0):
    if minimum == 0:
        return 0
        
    if len(l) == 1:
        sa = ps + l[0]
        sb = total - sa
        
        res = abs(sa - sb)
        if minimum > res:
            minimum = res
         
        if minimum == 0:
            return 0
            
        return minimum

    return min(
        solver(l[1:], minimum, ps), 
        solver(l[1:], minimum, ps+l[0])
    )
    
    
print(solver(a, total, 0))
