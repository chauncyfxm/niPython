



'''
for i in range(2,101):
	x = 1
	if i % 1 == 0 or i % i == 0 and i > 1:
			if i % x == 0:
				continue
			else:
				print(i)
'''






for i in range(2,101):
	myif = 0 
	for j in range(2,i):
		
		if i % j == 0 :
			myif = 1
			break
	if myif == 0:
		print (i)
