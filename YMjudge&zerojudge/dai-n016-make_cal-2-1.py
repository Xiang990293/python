all = input()
all = all.replace(" ", "")
while True:
	if all=="EOF":
		break
	if all.find("/")!=-1:
		if all[all.find("/")+1]=="0":
			print("nan")
		else:
			print(format(eval(all), '.6f'))
	elif all.find("%")!=-1:
		if all[all.find("%")+1]=="0":
			print("nan")
		else:
			print(eval(all))
	else:
		print(eval(all))
	
	all = input()
	all = all.replace(" ", "")

# all = input()
# all = all.split(" ")

# # before python 3.10
# while True:
# 	try:
# 		a = int(all[0])
# 		symble = str(all[1])
# 		b = int(all[2])
# 		if symble == "+":
# 			print(a+b)

# 		elif symble == "-":
# 			print(a-b)
				
# 		elif symble == "*":
# 			print(a*b)
				
# 		elif symble == "/":
# 			if b==0:
# 				print(0)
# 			else:
# 				print(format((a/b), '.6g'))
				
# 		elif symble == "%":
# 			if b==0:
# 				print(0)
# 			else:
# 				print(a%b)
		
# 		all = input()
# 		all = all.split(" ")
# 	except:
# 		break

# #after python 3.10
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