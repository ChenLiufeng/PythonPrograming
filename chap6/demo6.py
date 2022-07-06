# coding:utf-8
# @Time : 2022/6/13 19:27 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm
s1={20,10,30,40}
s2={20,30,40,50,60}
#交集
print(s1.intersection(s2))
print(s1&s2)

#并集操作
print(s1.union(s2))
print(s1|s2)

#差集
print(s1.difference(s2))
print(s1-s2)

#对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)
