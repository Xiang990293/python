def division(a, b):
    if b == 1:
        return a
    
    
    if bin(b)[-1] == 0:
        if bin(a)[-1] == 0:
            return division(a >> 1, b >> 1)
            