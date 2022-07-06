# coding:utf-8
# @Time : 2022/6/14 15:38 
# @Author : clf
# @File : demo11.py.py 
# @Software: PyCharm
#格式化字符串
#（1）%占位符
name='张三'
age=30
print('我叫%s,今年%d岁'%(name,age))
#（2）{}
print('我叫{0},今年{1}岁'.format(name,age))
#(3)f-string
print(f'我叫{name},今年{age}岁')
