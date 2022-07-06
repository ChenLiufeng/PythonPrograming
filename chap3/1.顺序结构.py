# coding:utf-8
# @Time : 2022/4/20 15:27 
# @Author : clf
# @File : 1.顺序结构.py.py 
# @Software: PyCharm

name = '张三' #将'张三'赋值为变量name
age = 20 #将20赋值为变量age

a=b=c=d=100 #将a,b,c,d的值同时赋值为100，链式赋值
#系列解包赋值
name1,age1='李四',22 #元组分解赋值

[name2,age2]=['王五',30] #列表分解赋值

a,b,c,d = 'room' #字符串分解赋值
print(a)
print(b)
print(c)
print(d)
#扩展的字符串解包赋值
a,*b='room'
print(a)
print(b)
