# coding:utf-8
# @Time : 2022/6/13 18:12 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm
s={2,3,4,5,6,7,8,9}#集合中元素不允许重复
print(s)
#可以将列表和元组都转成集合，集合内容是无序的
s1=set(range(6))
print(s1)

print(set([2,3,53,56]),type(set([2,3,53,56])))
print(set((2,3,53,56,4,2,3)),type(set((2,3,53,56,4,2,3))))
print(set('python'),type(set('python')))

print(10 in s)
s.add(110)
print(s)
s.update({100,300,500})
print(s)
s.update([100,90,34])
s.update((80,30,45))
print(s)
