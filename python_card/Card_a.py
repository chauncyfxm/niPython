str = "名片系统"
print(str.center(30,"*"))
list=[]

#增加
def addcard():
	name = input('请输入名字：')
	age = input('请输入年龄：')
	sex = input('请输入性别：')
	work = input('请输入工作：')
	address = input('请输入地址：')

	dictionary = {'name':name,'age':age,'sex':sex,'work':work,'address':address}
	list.append(dictionary)
	
	for i in list:
		print(i)
		return i



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
				print(i)
				break
	return list




#修改

def rvise():

	'''
	list = []
	list.append(addcard())
	'''
	oldValue = input('请输入要改的原有内容：')
	value = input('请输入要修改的内容：')
	for i in list:
		for y,j in i.items():
			if j == oldValue:
				i[y] = value
				print('修改后的内容是：')
				print(i)
				break
	return list








#######################   以下是正文，上面是函数   #########################



while True:
	mode = int(input('请选择功能 1.新增 2.修改 3.查询 4.删除 5.退出'))

	if mode == 1:
		addcard()
	elif mode == 4:
		delcard()
	elif mode == 2:
		rvise()
	elif mode == 3:
		for i in list:
			print(i)
	elif mode == 5:
		break




