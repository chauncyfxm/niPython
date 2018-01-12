list = [{'beijing':{'mianji':1290,'remkou':123},'shanghai':{'mi    anji':12331,'renkou':123123}}]
for i in list:
	for k,v in i.items():
		for y,wo in v.items():
			print(k,y,wo)
