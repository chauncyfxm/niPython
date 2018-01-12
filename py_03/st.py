import random
x = int(input('请输入：石头：1 ，剪刀: 2 ， 布：3    按:'))
y = random.randint(1,3)
y1 = '石头'
y2 = '剪刀'
y3 = '布'

'''
if x < y and y != 3 and y != 1 and x != 2:
	print ('电脑是:%s,你赢了!'%y2)
elif x < y and y != 2 and y != 1 and x != 2:
	print ('电脑是:%s,你输了!'%y3)
elif x < y and y != 2 and y != 1 and x != 1:
	print ('电脑是%s,你输了！'%)
'''
if x <= 3 and x >= 1:
	if (x ==1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
		print ('你输')
	elif (x ==1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
		print ('你赢')
	else:
		print ('平局')
	
	
	
	
	
	
	
	if y == 1:
		y1 = '石头'
		print('电脑是%s'%y1)
	elif y== 2:
		y2 = '剪刀'
		print('电脑是%s'%y2)
	elif y== 3:
		y3 = '布'
		print('电脑是%s'%y3)
else:
	print('请输入合法字')







