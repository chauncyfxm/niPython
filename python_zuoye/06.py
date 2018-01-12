

pro = 0



for i in range(0,10):
	for y in range(1,i+1):
		pro = y * i
		print('\t%d * %d = %d  '%(y,i,pro), end = '')
	print('')
