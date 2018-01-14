str = '欢迎进入QQ炫舞换装系统'

print(str.center(30,'*'))

def begin():
	while True:
		account = 'xiaona'
		passwd = 'xiaonana'


		myaccount = input('请输入账号：\t') 
		mypasswd = input('请输入密码：\t')



		if myaccount == account and mypasswd == passwd:
			print('登录成功')
			print('开始游戏')
			while True:
				option = int(input('请选择你要干什么：1、查看装备，2、更换装备，3、清理过期装备，4、购买装备，5、退出'))
				if option == 1:
					check()
				elif option == 2:
					change()
				elif option == 3:
					remove()
				elif option == 4:
					buy()
				elif option == 5:
					break
		elif myaccount != account and mypasswd != passwd:
			print ('你输入的账号密码不正确，请重新输入！,按ESC键退出!') 
			continue






myclotthes = ['水瓶星露礼裙','魅蓝星舞羽翼']
Myentr = ['樱花公主套裙','魅蓝星舞羽翼','凝芬苏韵礼裙','曙光之羽翼','音阶律恋服饰','轻盈似梦礼服','水麟浅月礼服']
store = ['琉璃诗梦礼裙','河韵号思礼裙','闭月羞花礼裙','水瓶星露礼裙','朝花夕拾礼裙','紫星怡暖羽翼','碧空雨蝶羽翼','芳菲若韵羽翼','苍蓝蝶舞羽翼']
def check():
	print('你的原有装备是:')
	for i in Myentr:
		print(i.center(30,'*'))
	print('商城的装备有:')
	for y in store:
		print(y.center(25,'-'))





def change():
	print('当前的您的衣物为：')
	for i in myclotthes:
		print(i.center(30,'~'))
	option = int(input('请挑选你的衣物：1、衣物，2、羽翼：'))
	if option == 1:
		print('你的仓库有：')
		for y in Myentr:
			index = int(Myentr.index(y))
			print(index+1)
			print(y.center(30,'-'))
		option1 = int(input('请选择衣物号：'))
		print('女神蜕变成功！')
		print('您更换后的衣物为：')
		myclotthes[0] = Myentr[option1-1]
		for y in myclotthes:
			print(y.center(30,'~'))
			
			






def remove():
	print('你的仓库有：')
	
	for i in Myentr:
		index = Myentr.index(i)
		print(index+1)
		print(i.center(30,'~'))
	option = int(input('请选择你要删除的衣物：'))
	print('是清理的装备是：')
	print(Myentr[option-1])
	Myentr.pop(option-1)
	for i in Myentr:
		print(i.center(30,'~'))







def	buy():
	print('商城里有：')
	for i in store:
		index = int(store.index(i))
		print(index+1)
		print(i.center(30,'~'))
	option = int(input('请选择你购买的衣物号：'))
	Myentr.append(store[option-1])
	print('你增加的衣物是：')
	print(store[option-1])
	print('你的仓库购买后的衣物是：')
	for i in Myentr:
		print(i.center(30,'*'))



begin()
