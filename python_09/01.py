def sum(a=100,mode = 0 ):
	sum1 = 0
	if not mode:
		for i in range(1,a+1):
			sum1 += i
	else:
		count = 1
		while count < a+1:
			sum1 += count
			count += 1
	
	print(sum1)
	return sum1

sum(100,1)
