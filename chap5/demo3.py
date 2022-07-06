# coding:utf-8
# @Time : 2022/6/13 15:27 
# @Author : clf
# @File : demo3.py.py 
# @Software: PyCharm
scores={'Jack':29,'Mark':98,'Frank':90}
#判断是否在字典里面
print('Frank' in scores)
print('marry' not in scores)
#增加元素
scores['Marry']=100
print(scores)
#修改元素
scores['Frank']=120
print(scores)

#删除元素
del scores['Marry']
print(scores)

#获取所有的key
keys=scores.keys()
print(type(keys))
print(keys)
print(list(keys)) #将所有的key组成的视图转成列表

values = scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value对

items = scores.items()
print(items)
print(type(items))
print(list(items))

for item in scores:
    print(item)
    print(item,scores[item],scores.get(item))