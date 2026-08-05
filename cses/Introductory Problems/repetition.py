string = input()

prev = string[0]
remain = string[1:]

max = 1
counter = 1
for i in remain:
    if i == prev:
        counter += 1
    else:
        counter = 1
        prev = i
        
    if counter > max:
        max = counter

print(max)
