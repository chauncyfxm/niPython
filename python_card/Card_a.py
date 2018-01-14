str = "名片系统"
print(str.center(30,"*"))
list=[{'姓名':'冯新民','年龄':'24','性别':'男','工作':'AI','地址':'大兴'}]


def begin():
	while True:
		mode = int(input('请选择功能 1.新增 2.修改 3.查询 4.删除 5.退出'))

		if mode == 1:
			addcard()
		elif mode == 4:
			delcard()
		elif mode == 2:
			rvise()
		elif mode == 3:
			print_card()
		elif mode == 5:
			break

#增加
def addcard():
	dic = {}
	while True:
		name = input('请输入名字：')
		age = input('请输入年龄：')
		sex = input('请输入性别：')
		work = input('请输入工作：')
		address = input('请输入地址：')
		dic = {'姓名':name,'年龄':age,'性别':sex,'工作':work,'地址':address}
		list.append(dic)
		print_card()
		break




#打印列表	
def print_card():
	for y in list:
		for i,i1 in y.items():
			if i == '姓名':
				print('%s : %s'%(i,i1.center(20,'~')))
		for i,i1 in y.items():
			if i == '年龄':
				print('%s : %s'%(i,i1.center(20,'~')))
		for i,i1 in y.items():
			if i == '性别':
				print('%s : %s'%(i,i1.center(20,'~')))
		for i,i1 in y.items():
			if i == '工作':
				print('%s : %s'%(i,i1.center(20,'~')))
		for i,i1 in y.items():
			if i == '地址':
				print('%s : %s'%(i,i1.center(20,'~')))
		print('-'*10)


#删除
def delcard():
	'''
	list = []
	list.append(addcard())
	'''
	name = input('请输入你要删除的名片组的姓名：')
	for i in list:
		for k,j in i.items():
			if k == 'name' and j == name:
				TempIndex = True 
				TempIndex = list.index(i)
				list.pop(TempIndex)
				print('删除后的内容是：')
				
				break
	return list




#修改

def rvise():

	'''
	list = []
	list.append(addcard())
	'''
	while True:
		oldValue = input('请输入要改的原有内容的姓名：')
		print('你要修改的内容是：')
		judge = False
		for i in list:
			for y,j in i.items():
				if j == oldValue:
					for i1,i2 in i.items():
						print(i1.center(10,'~'))
						print(i2)
						judge = True
		if judge:
			break
		else:
			print('名片系统里没有这个内容,你重新输入吧!')
	value = input('请输入要新的内容：')
	for i in list:
		for y,j in i.items():
			if j == oldValue:
				i[y] = value
				print('修改后的内容是：')
				for i1,i2 in i.items():
					print(i1.center(10,'~'))
					print(i2)
				break
	return list









begin()



