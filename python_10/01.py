def number(a):
	if a >1:
		return a * number(a-1)
	else:
		return a
print(number(5))




def sum(a,b):
	def sum1(c):
		return a+b+c
	return sum1



resuat = sum(1,2)
b = resuat(10)



def Mysum(a,b):
	return a+b



print(Mysum(10,20))

