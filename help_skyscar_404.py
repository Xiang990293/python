#設立空tuple atuple
atuple = ()

#迴圈(不特定重複次數/有條件重複 => while)
temp = 1 #預設=0就不會執行了
while True: #一直執行下去，除非被 break
	temp = input("Please enter an integer (0 to exit): ") #詢問及條件，注意空格
	
	try: #試試看，出錯會跳到 except
		if temp != int(temp): #是否是整數，不是就不做任何事
			if int(temp) == 0: #如果是0就跳出迴圈，使用 break
				break
			else:
				atuple += tuple((int(temp),)) #把新數字加入 atuple
				print(atuple) #列印 atuple
	except:
		exit #不做任何事，不加電腦不會知道
	
	
	
	
	