# coding:utf-8
# @Time : 2022/6/13 22:08 
# @Author : clf
# @File : demo8.py.py 
# @Software: PyCharm
s='hello Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

lst=['hello','java','Python']
lst1='|'.join(lst)
print(type(lst1))
print('|'.join(lst))
print(''.join(lst))