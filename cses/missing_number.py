max: int = int(input(""))
nset: set = set(map(int, input("").split(" ")))

all = set(range(1, max+1))
print(all.difference(nset).pop())