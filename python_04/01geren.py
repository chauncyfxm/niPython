x = '欢迎进入个人管理信息系统'
print(x.center(40,'*'))

zongde = []


while True:
	bianhao = int(input('请输入1录入，2查询，3修改，4删除'))
	if bianhao == 1:

		name = input('请输入名字：')
		age = int(input('请输入年龄：'))
		sex = input('请输入性别：')
		gongzuo = input('请输入工作：')



		zongde.append(name)
		zongde.append(age)
		zongde.append(sex)
		zongde.append(gongzuo)


		print(zongde)
		
	elif bianhao == 2:

		index = int(input('请输入索引：'))

		print(zongde[index])

	elif bianhao == 3:
		gaiming = input('请输入修改的名字：')
		xingaiming = input('请输入新的名字')
		zongde[0] = xingaiming

		print(zongde)

	elif bianhao == 4:

		delname = input('请输入你要删除的名字')


		del zongde[0]

		print('删除成功')
		print(zongde)
	else:
		print('错误')
