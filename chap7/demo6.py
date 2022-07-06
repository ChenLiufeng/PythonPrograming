# coding:utf-8
# @Time : 2022/6/13 21:40 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm
s='hello world python'
lst=s.split() #默认从空格开始劈分
print(lst)
s1='hello|world|python'
print(s1.split(sep='|')) #默认从左侧开始劈分
print(s1.split(sep='|',maxsplit=1))

print(s.rsplit()) #默认从右侧开始劈分