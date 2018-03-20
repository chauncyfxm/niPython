import random

class FengXinMin_game(object):

	def __init__(self):
		self.int = 0
		self.count_w = 0
		self.count_d = 0

	def FengXinMin_Cai(self):
		self.int = random.randint(0,20)
		print(self.int)
		self.count_w += 1

		self.count_d = 0

		while True:
			self.count_d += 1

			FengXinMin_int = int(input("请输入一个整数看看你输入的数字是对的还是错的："))
			print(FengXinMin_int)

			if FengXinMin_int > self.int:
				print("你猜错了，比我的数字大了,再猜猜吧！")
			elif FengXinMin_int < self.int:
				print("你猜错了，比我的数字小了,再猜猜吧！")
			else:
				print("你猜对了，我的数字就是" + str(self.int))
				break
		print("一共玩了：%d 局游戏"%self.count_w)
		print("本局猜了：%d 次"%self.count_d)








FengXinMin_CaiZi = FengXinMin_game()




try:
	while True:
		FengXinMin_count = int(input("输入1开始游戏："))
		if FengXinMin_count == 1:
			FengXinMin_CaiZi.FengXinMin_Cai()
		else:
			break
except:
	print("你选择了退出游戏，再见！")


