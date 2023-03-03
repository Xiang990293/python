from math import sqrt

def is_perfect_square(i):
    if(sqrt(i)/1==sqrt(i)//1):
        return True
    else:
        return False

for i in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    if(is_perfect_square(i)):
        hundrad = int(str(i)[0:-2])
        ten = int(str(i)[0:-1])
        if(is_perfect_square(hundrad)&is_perfect_square(ten)):
            print(i)
print("program ended")
