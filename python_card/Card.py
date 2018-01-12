def AddCard():
	Newcard = {}
	card = {}
	cardList = []

	while True:
		name = input('请输入名字：')
		age = input('请输入年龄:')
		TempList = []
		for i in cardList:
			for keys in i:
				TempList.append(i[keys])
		a = TempList.count(name)   #a 是临时用来判断的
		#a = TempList.find(name,0,len(TempList)) 
		if a == 0:
			card = {'name':name,'age':age}
			#Newcard.update(card)
			cardList.append(card)
			print(cardList)


			for i in cardList:
				for keys in i:
					print(keys,i[keys])
			
		else:
			print('你输入的重复了,请重新输入')
			continue


AddCard()
