# coding:utf-8
# @Time : 2022/6/13 14:10 
# @Author : clf
# @File : demoremo.py.py 
# @Software: PyCharm
lst=[10,20,30,40,50,60,30]
lst.remove(30) #从列表中删除一个元素，如果有重复元素只移除第一个元素
print(lst)
#
# lst.remove(100) #ValueError: list.remove(x): x not in list 元素不存在就抛异常
# print(lst)

lst.pop(1) #pop()根据索引移除元素，索引位置不存在，就抛异常
print(lst)

lst.pop()
print(lst) #如果不指定参数，将删除列表中的最后一个元素

print('*************切片操作-删除至少一个元素*产生新列表****************')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)

lst[1:3] = []
print(lst)

lst.clear()
print(lst)

del lst
print(lst)