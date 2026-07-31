ind = "abcdefghijklmnopqrstuvwxyz"
def val(char):
    if char not in ind:
        return -1
    return ind.find(char)

def sort(l, leng):
    if leng < 2:
        return l
    
    left = sort(l[:leng//2], leng//2)
    right = sort(l[leng//2:], leng-leng//2)
    result = []
    
    while left and right:
        if val(left[0]) < val(right[0]):
            result += left[0]
            left.pop(0)
        else:
            result += right[0]
            right.pop(0)
            
    if left:
        result.extend(left)
    elif right:
        result.extend(right)
    return result
    
def l2s(l: list)-> str:
    if len(l) == 1:
        return l
    head = l[0]
    
    res = []
    for i in perm(l[1:]):
        res.append(head + i)
    
    return res
    
def perm(l: list):
    """
        wrong
    """
    
    if len(l) == 1:
        return l
    head = l[0]
    
    res = []
    for i in perm(l[1:]):
        res.append(head + i)
    
    return res

s = input()
rs = set([])
s = list(s)
s = sort(s, len(s))
print(perm(s))
