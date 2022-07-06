# coding:utf-8
# @Time : 2022/6/13 20:54 
# @Author : clf
# @File : demo3.py.py 
# @Software: PyCharm

#字符串中的大小写转换的方法,转换会成为一个新的字符串对象
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))

print(s.lower(),id(s.lower()))

s2='hello,Python'
print(s2.swapcase())
print(s2.title())