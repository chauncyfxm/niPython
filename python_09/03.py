





def prime_number(value):
	prime_number1 = []
	for i in range(2,value+1):
		myif = True
		for y in range(2,i):
			if i % y == 0:
				myif = False
		if myif:
			prime_number1.append(i)
	print(prime_number1)
	return prime_number1
prime_number(100)
