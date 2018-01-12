ZhangHao = input('账号：')
MiMag = input('密码：')
XingMing = input('姓名：')
TiQuShu = int(input('提取金额：'))
YuanYouJinE = 100000



YuanYouJinE = YuanYouJinE - TiQuShu


print ('尊敬的%s，你提取了%.2f元，剩余%.2f元，再见！'%(XingMing,TiQuShu,YuanYouJinE,))
