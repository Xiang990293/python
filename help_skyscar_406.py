import cmath

#設立空清單
templist = []
resultlist = []

while True:
	templist = [] #預設為空
	resultlist = [] #預設為空
	templist += input("請輸入一個清單: ").replace("[","").replace("]","").replace(" ","").replace("\'","").split(",") #把空格上下方括弧去掉，再用逗號當分隔符號將字串分開
	for i in templist: #在 templist 中取值設為 i
		if i.isdigit(): #是整數
			resultlist+=[int(i),]
			continue #直接進到下一個 i
		if i.isalpha(): #是字串
			resultlist+=[str(i),]
			continue
		try:
			if isinstance(float(i), float): #是小數
				resultlist+=[float(i),]
				continue
		except ValueError:
			try:
				if isinstance(complex(i), complex): #是複數
					resultlist+=[complex(i),]
					continue
			except ValueError:
				exit
		
	print(resultlist)