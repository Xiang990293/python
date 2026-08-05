n = int(input())

i = 1
s = "0"
r = ["0", "1"]
while i < n:
    i += 1
    r0 = r[::-1]
    r = list(map(lambda x: x.zfill(i), r))
    for j in r0:
        r.append("1"+j)
    
for j in r:
    print(j.zfill(n))
