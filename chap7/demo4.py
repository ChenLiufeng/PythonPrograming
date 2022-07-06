# coding:utf-8
# @Time : 2022/6/13 21:31 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm
s='hello,Python'
print(s.center(20,'*')) #居中对齐
print(s.ljust(20,'*')) #左对齐
print(s.ljust(10)) #默认填充空格
print(s.ljust(20))#默认填充空格

print(s.rjust(20,'*'))
print(s.rjust(20))

#右对齐，使用0进行填充
print(s.zfill(20))
print('-8910'.zfill(8)) #包括减号一共八位