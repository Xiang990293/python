n = int(input())
a = list(map(int, input().split(" ")))
b = []
prevres, res = None, None

def nearest(l, f):
    leng = len(l)
    
    if leng == 1:
        return 0, l[0]
        
    mid = leng//2
    
    
    
    if f == l[mid]:
        return mid, f
    
    if f > l[mid]:
        delta, val = nearest(l[mid:], f)
        return mid + delta, val
    if f < l[mid]:
        delta, val =  nearest(l[:mid], f)
        return delta, val

while True:
    sa = sum(a)
    if b == []:
        sb = 0
    else:
        sb = sum(b)
    if sa < sb:
        a, b = b, a
        sa, sb = sb, sa
        
    a.sort()
    b.sort()
    
    dsab = (sa - sb)
    fhdsab = dsab / 2
    hdsab = dsab//2
    if sa == sb:
        res = 0
        break
    
    
    prevres = res
    sind, _ = nearest(a, fhdsab)
    for i in a[:sind+1][::-1]:
        if fhdsab - i < 0:
            break
        res = fhdsab - i
        if i in a and prevres is None:
            b.append(i)
            a.remove(i)
            break
            
        elif i in a and prevres > res:
            b.append(i)
            a.remove(i)
            break
        
    
    if prevres == res and res is not None:
        break
    
    
print(sa - sb)

