# coding:utf-8
# @Time : 2022/4/20 10:55 
# @Author : clf
# @File : 7.布尔类型.py 
# @Software: PyCharm
x = True
print(x)
print(type(x))
print(True + 10) #1+10
print(False + 10) #0+10

print('----------------------------------')
print(bool(18)) #True
print(bool(0),bool(0.0)) #False
print(bool('')) #False
print(bool(False)) #False
print(bool(None))#False