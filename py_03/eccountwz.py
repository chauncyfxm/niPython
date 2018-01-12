account = '冯新民'
passwd = '123456'

my_account = input('请输入你的账号：')
my_passwd = input('请输入你的密码：')
x = 0

while x < 100:
	if my_account == account and my_passwd == passwd:
		name = int(input('请输入英雄范围：0代表ADC、1代表肉、2代表法师     按：'))
		if name == 0:
			name0 = '鲁班大师'
			print ('请使用鲁班大师')
		elif name == 1:
			print ('请使用陈咬金')
			name1 = '陈咬金'
		elif name == 2:
			print ('请使用王昭君')
			name2 = '王昭君'
	x +=1

else:
	print('你输入的账号或密码错误，请重新输入！')
