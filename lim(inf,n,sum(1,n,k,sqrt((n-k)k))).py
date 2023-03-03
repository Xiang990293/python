import math

i=100
k=0
dk=0
while(True):
    i+=1
    k2=0
    for j in range(i):
        k2+=math.sqrt((i-j)*j)
    dk2=k2-k
    ddk2=dk2-dk
    print(i,k2,dk2,ddk2)
    k=k2
    dk=dk2