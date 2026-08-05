nu = input("")
nlist = list(map(int, input("").split(" ")))

counter = 0
prev = nlist[0]
remain = nlist[1:]
for i in range(len(remain)):
    if prev > remain[i]:
        counter += prev - remain[i]
    else:
        prev = remain[i]
    
print(counter)
