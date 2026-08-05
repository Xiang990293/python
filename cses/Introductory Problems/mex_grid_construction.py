n = int(input())

def solver(n):
    if n == 1:
        return [[0]]

    res = solver(n - 1)

    start = res[0][-1] + 1
    temp = []
    if n % 2 == 1:
        for i in range(n - 1):
            res[i].append(start + i)
            temp.append(start + i)

        temp.append(0)
        res.append(temp)

        return res

    res[0].append(start)
    temp.append(start)
    for i in range(1, n - 1):
        all = set(range(2*n + 1))

        above = set(list(map(lambda x: x[-1], res[:i])))
        left = set(res[i])
        exs = above.union(left)
        num = min(all.difference(exs))
        res[i].append(num)
        temp.append(num)

    temp.append(0)
    res.append(temp)

    return res


res = solver(n)
for i in res:
    print(str(i).replace("[","").replace("]","").replace(",",""))