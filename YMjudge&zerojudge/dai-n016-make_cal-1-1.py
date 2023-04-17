all = input()
all = all.split(" ")

# before python 3.10
while True:
	try:
		symble = str(all[0])
		a = int(all[1])
		b = int(all[2])
		if symble == "+":
			print(a+b)

		elif symble == "-":
			print(a-b)
				
		elif symble == "*":
			print(a*b)
				
		elif symble == "/":
			print(format((a/b), '.6g'))
				
		elif symble == "%":
			print(a%b)
		
		all = input()
		all = all.split(" ")
	except:
		break

# after python 3.10
# while True:
# 	try:
# 		symble = str(all[0])
# 		a = int(all[1])
# 		b = int(all[2])
# 		print(c)
# 		match symble:
# 			case "+":
# 				print(a+b)

# 			case "-":
# 				print(a-b)
				
# 			case "*":
# 				print(a*b)
				
# 			case "/":
# 				print(format((a/b), '.6g'))
				
# 			case "%":
# 				print(a%b)
		
# 		all = input()
# 		all = all.split(" ")
# 	except:
# 		break

inp=input()
while True:
	if inp=="EOF":
		break
	a=1
	b=1
	inp=int(inp)
	print("1 | 1")
	print("2 | 1")
	if inp==2:
		print("1")
		print("黃金比例：1")
	else:
		for i in range(inp-2):
			c=a
			b+=a
			a=b
			b=c
			print(i+3, "|", a)
		print(a)
		print("黃金比例："+format((a/b), '.6g'))
		
	inp = input()