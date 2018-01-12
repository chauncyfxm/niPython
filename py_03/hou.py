jsum = 0
osum = 0
zsum = 0
x = 0
y = 0
while x < 100:
	x += 1
	if x % 2 != 0:
		jsum += x
while y < -100:
	y -= 1
	if y % 2 == 0:
		osum += y
zsum = jsum + osum
print('老师要的结果是：%d'%zsum)
