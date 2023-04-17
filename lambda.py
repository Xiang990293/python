todict=input("請輸入英文:中文字典翻譯字彙(輸入0:0結束) -> ")
dicti = {}

while(todict!="0:0"):
	if len(todict.split(":"))==2:
		try:
			todict=todict.split(":")
			dicti.update({todict[0]:todict[1]})
		except ValueError:
			todict=input("請輸入英文:中文字典翻譯字彙(輸入0:0結束) -> ")
			continue
	todict=input("請輸入英文:中文字典翻譯字彙(輸入0:0結束) -> ")

print(dicti)