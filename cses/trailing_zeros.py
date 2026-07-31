n = int(input())

if n < 5:
    print(0)

i = 5
result = 0
while i <= n:
    result += n//i
    i *= 5
    
print(result)
