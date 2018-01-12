x2 = 0

product = 0
y1 = 0
y2 = 0


while x2 < 5:
	x1 = 0
	while x1 < x2+1:
		#print('*',end = '')
		x1 += 1
		y2 = x2 + 1
		y1 = x1 
		product = y1 * y2
		print ('%d * %d = %d '%(y1,y2,product), end = '')
	x2 += 1
	print('')
