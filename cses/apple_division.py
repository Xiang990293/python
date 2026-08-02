import numpy

n = int(input())
a = list(map(int, input().split(" ")))

total = sum(a)
minimum = None

"""
This is the brute force method, 
the old one with wrong answer got removed, 
check the old file preview instead if needed.
"""

def find_masum(b: int):
    vec = list(map(int,tuple(bin(b).replace("0b","").zfill(n))))
    return numpy.dot(numpy.array(vec), numpy.array(a))
    

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
