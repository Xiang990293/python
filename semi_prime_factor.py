import math

w = int(input("Enter a semi-primenumber: "))
while w<=0:
    w = int(input("Enter a semi-primenumber: "))

for i in range(10**int(math.ceil(math.log(math.sqrt(w),10))),4,-1):
    if math.sqrt(abs(i**2 - w))%1==0:
        print(int(i+math.sqrt(abs(i**2 - w))), int(i-math.sqrt(abs(i**2 - w))))
        break
else:
    print("pair not found")