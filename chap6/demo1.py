#coding:utf-8
# @Time : 2022/6/13 17:27 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm
'''不可变序列，可变序列'''

'''可变序列：列表和字典,增加和删除操作，内存地址不会变'''
lst =[10,20,30]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列，字符串，元组,内存地址会改变的'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))