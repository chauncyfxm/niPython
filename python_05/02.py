list = [{'beijing':{'mianji':1290,'remkou':123},'shanghai':{'mianji':12331,'renkou':123123}}]


for i in list:
	for y in i:
		liebiao = i[y]
		for a in liebiao:
			print(y,a,liebiao[a])
