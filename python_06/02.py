def Mysum():
	jsum = 0
	osum = 0
	zsum = 0



	for i in range(1,101):
		if i % 2 == 0:
			osum = i + osum
		if i % 2 != 0:
			jsum = i + jsum
		zsum = i + zsum
	print('总数是%d,奇数是%d,偶数是%d'%(zsum,osum,jsum))


Mysum()
