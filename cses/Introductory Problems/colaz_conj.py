concate = ""
current = int(input(""))
while current != 1:
  concate += str(int(current)) + " "
  if current % 2 == 0:
      current /= 2
  else:
      current *= 3
      current += 1
concate += "1"
print(concate)