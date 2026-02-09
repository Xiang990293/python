N = 9797
e = 1001
plain = ["3500", "0801", "2205", "0019", "1513", "0500", "0116", "1612", "0519"] # 不足可以補零，但這次不需要

encrypt = ""
for segment in plain:
  encrypt += "{:04d}".format(int(segment) ** e % N)
  
print(encrypt)


f = 7001

listify = [encrypt[0+4*i:4+4*i] for i in range(len(encrypt)//4)]

plain = ""
for segment in listify:
  plain += "{:04d}".format(int(segment) ** f % N)
  
print(plain)