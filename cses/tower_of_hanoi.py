n = int(input())

hanoi = [
    [],
    list(range(n)),
    [],
    []
    ]

def solver(ini, lax, tar, n):
    if n == 0:
        return
    
    solver(ini, tar, lax, n-1)
    hanoi[tar].append(hanoi[ini].pop())
    print(ini, tar)
    solver(lax, ini, tar, n-1)
    
    return

print(2**n-1)
solver(1, 2, 3, n)
