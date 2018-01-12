import random









while True:
	q = random.randint(1,2)
	if q ==1:
		x = '大'
	elif q == 2:
		x = '小'



	my = input('请输入：大或小     输入：')


	if my == x:
		print('你猜对了，电脑是:%s\n游戏结束'%x)
		break
	else:
		print('猜错了请重新输入,电脑是:%s'%x)








