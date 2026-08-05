n = int(input())

def solver(n):
    if n == 0:
        return [0]

    res = solver(n - 1)

    start = res[0][-1]+1
    temp = []
    if n % 2 == 0:
        for i in range(n - 1):
            res[i].append(start + i)
            temp.append(start + i)

        res.append(temp.append(0))

        return res

    res[0].append(start)
    temp.append(start)
    for i in range(1, n - 1):
        
