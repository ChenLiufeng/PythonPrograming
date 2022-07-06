# coding:utf-8
# @Time : 2022/6/13 13:57 
# @Author : clf
# @File : listadd.py.py 
# @Software: PyCharm

lst=[10,20,30]
print('添加之前',lst,id(lst))
lst.append(40)
print('添加之后',lst,id(lst))

lst2=['hello','world']
# lst.append(lst2) #把lst2作为一个元素添加到列表的末尾
# print(lst)

lst.extend(lst2) #在列表的末尾一次性添加多个元素
print(lst)

#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)

lst3=['True','False','hello']
#在任意位置上添加多个元素
lst[1:]=lst3
print(lst)