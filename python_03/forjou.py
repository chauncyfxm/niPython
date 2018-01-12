jsum = 0
osum = 0
zsum = 0






for i in range(0,101):
	if i % 2 == 0:
		osum += i 
	elif i % 2 != 0:
		jsum += i
	zsum +=i
print(jsum,osum,zsum)
