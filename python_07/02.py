

def sum(a,b,c):
	print(a + b, a - c)









sum = 0
for i in range(100,200):
	a = True
	for y in range(2,i):
		if i % y == 0:
			a = False
			break
	if a == True:
		sum += i
print(sum)



