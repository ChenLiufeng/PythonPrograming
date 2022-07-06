# coding:utf-8
# @Time : 2022/6/13 17:13 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm
items=['Fruits','Book','Others']
prices=[96,78,85]
d={ item.upper():price for item,price in zip(items,prices)} #key值为大写
d1={item:price for item,price in zip(items,prices)}
print(d)
print(d1)