import math

def insert(raw: str, index: int, char: str):
    return raw[:index] + char + raw[index:]

def solver(source: str):
    result = ""
    cand = []
    for c in source:
        if c not in cand :
            cand += c
        elif c in cand:
            cand.remove(c)
            result += c
    
    if len(cand) > 1:
        return "NO SOLUTION"
    
    result += cand[0]
    
    return result + result[:-1][::-1]
    
print(solver(input()))
