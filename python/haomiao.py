year = 1
month = 1
dey = 1
hour = 1
minute = 1
second = 1
haomiao = 1

'''
#没用的代码不用管
month = year * 12
dey = month * 30
hour = dey * 24
minute = hour * 60
second = minute * 60
haomiao = second * 1000
'''
a = year
haomiao = (a * 12 * 30 * 24 * 60 * 60 * 1000)

print ('一年等于%d毫秒'%haomiao)
#print ('1天等于:'+dey*24*60*60*1000)





a1 = month
haomiao = (a * 30 * 24 * 60 * 60 * 1000)
print ('一个月等于：' + str(haomiao) + '毫秒')





