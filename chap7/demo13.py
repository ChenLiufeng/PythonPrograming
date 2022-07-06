# coding:utf-8
# @Time : 2022/6/14 15:58 
# @Author : clf
# @File : demo13.py.py 
# @Software: PyCharm
print('%10d'%99) #10表示的是宽度

print('%.3f'%3.1415926) #.3表示是小数点后三位

print('%10.3f'%3.1415926) #一共总宽度为10，小数点后3位

print('{0:.3}'.format(3.1415926))#.3表示一共是3位
print('{0:.3f}'.format(3.1415926)) #.3f表示3为小数
print('{0:10.3f}'.format(3.1415926)) #同时设置宽度和精度，一共是10位，小数为3位。