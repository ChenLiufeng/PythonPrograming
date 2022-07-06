# coding:utf-8
# @Time : 2022/6/13 11:19 
# @Author : clf
# @File : demolist1.py.py 
# @Software: PyCharm

lst=[10,20,30,40,50,60,70,80]
#print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))
#默认步长为1
print(lst[1:6:1])
print(lst[1:6]) #默认步长为1
print(lst[1:6:])

print(lst[1:6:2]) #步长为2
#stop默认为最后一个元素
print(lst[1::2])

#步长为负数的情况
print(lst[::-1])
print(lst[6:0:-2])