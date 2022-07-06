# coding:utf-8
# @Time : 2022/4/20 11:05 
# @Author : clf
# @File : 8.数据类型间的转换.py.py 
# @Software: PyCharm
x = 10
y = 3
z = x/y
print(z,type(z)) #隐式转换，通过运算隐式地转换了结果的数据类型

print('--------显式转换数据格式------------')
print('------float类型转换成int类型------------')
#float类型转换成int类型,只保存整数部分
print('float类型转换成int类型',int(3.14))
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.9))
print('float类型转换成int类型',int(-3.14))
#int类型转换成float类型
print('------int类型转换成float类型------------')
print('int类型转换成float类型',float(3))
#str类型转换成int类型
print('------str类型转换成int类型------------')
print('str类型转换成int类型',int('100')+int('240'))
#str类型转换成float类型
print('------str类型转换成float类型------------')
print('str类型转换成float类型',float('3.14'))
#将str转成int或float类型报错的情况：str里面带有字母都其他字符
#将str转成float类型报错的情况

#chr()函数和ord()函数
name = '陈'
print(ord(name)) #将字符串转换为对应的整数值，38472
print(chr(38472)) #将整数38472转换为对应的字符

#进制之间的转换操作，十进制与其他进制之间的转换
print('十进制转换为十六进制：'+hex(x))
print('十进制转换为八进制：'+oct(x))
print('十进制转换为二进制：'+bin(x))