x = 0
jsum = 0
osum = 0
zsum = 0

while x < 100:
	zsum += x
	print (zsum)
	if x % 2 == 0:
		jsum += x 
		print(jsum)
	x += 1
	if x %2 !=0:
		osum += x
		print(osum)








print('*'*10)
print('0到100中的所有的偶数是%d,所有的奇数是%d,所有的数的和%d'%(osum,jsum,zsum))
