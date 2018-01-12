myaccount = '冯新民'
mypasswd = '12345'




while True:
	account = input('请输入你的账号：') 
	passwd = input('请输入你的密码：')


	if myaccount == account and passwd == mypasswd:
		print('欢迎来到王者世界！')	
		break
	else:
		print('你的账号或密码错误')
		print('*'*10,end = '')
		print('\n')
