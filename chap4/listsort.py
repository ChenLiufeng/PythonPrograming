# coding:utf-8
# @Time : 2022/6/13 14:26 
# @Author : clf
# @File : listsort.py.py 
# @Software: PyCharm
lst=[20,30,40,98,54]

print('排序前的列表',lst,id(lst))
lst.sort() #sort升序排序
print('排序后的列表',lst,id(lst))

lst.sort(reverse=True) #reverse=True,表示降序排序，reverse=False是升序排序
print(lst)

lst.sort(reverse=False) #reverse=True,表示降序排序，reverse=False是升序排序
print(lst)

print('***************使用内置函数sorted()对列表进行排序，会产生一个新的列表对象****************************')
lst=[20,30,79,45,90,12]
#开始排序，默认为升序排序
new_list=sorted(lst)
print(lst)
print(new_list)

desc_list=sorted(lst,reverse=True)
print(desc_list)