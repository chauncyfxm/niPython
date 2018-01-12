account = '1234'
passwd = 'abc'
money = 1000000.00



my_account = input('请输入你的账号：')
my_passwd = input('请输入你的密码：')




if my_account == account and my_passwd == passwd:
	print('*'*10)
	print('登录成功')
	print('*'*10)
	mode = int(input('请输入：1存、2取：'))
	if mode == 2:
		IMmoney = float(input('请输入你的金额：'))
		if IMmoney > money:
			print('你没这么多钱啊！')
		elif IMmoney < money+1:
			print ('你取了%.2f元钱，还剩%.2f元钱'%(IMmoney,money-IMmoney))
	elif mode == 1:
		pass
	else:
		print('你输入的不正却')
else:
	print('你的账号或者密码错误！')
