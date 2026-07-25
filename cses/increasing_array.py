nu = input("")
nlist = list(map(int, input("").split(" ")))

counter = 0
prev = nlist[0]
remain = nlist[1:]
for i in range(len(remain)):
    while prev > remain[i]:
        remain[i] += 1
        counter += 1
    prev = remain[i]
    
print(counter)