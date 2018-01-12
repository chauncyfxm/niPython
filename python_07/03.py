
def nian(n,y,r):
	t = 0

	if n % 4 == 0:
		if n % 100 != 0:
			a = 1
	elif n % 400 == 0:
		a = 1
	else:
		a = 0

	for i in range(1,y):
		if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i ==12:
			t += 31
		elif i == 2:
			if a == 0:
				t += 28
			elif a == 1:
				t += 29
		else:
			t += 30
	t = r + t
	print('%d年%d月%d日,是这一年的第%d天'%(n,y,r,t))
	return t

n = int(input('请输入年份：'))
y = int(input('请输入月份：'))
r = int(input('请输入日份：'))
nian(n,y,r)
