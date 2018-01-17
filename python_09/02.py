def sum(a,b,c,*args,**kwargs):
	sum1 = 0
	for i in args:
		sum1 += i
	for y,v in kwargs.items():
		sum1 += v
	sum1 += a+b+c
	print(sum1)
	return sum1



sum(1,2,3,4,1,32,1,age=1,age1 = 10,age2 = 23)
