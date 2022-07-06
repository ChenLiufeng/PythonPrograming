# coding:utf-8
# @Time : 2022/6/15 22:04 
# @Author : clf
# @File : demo7.py.py 
# @Software: PyCharm
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2
print(s)

print('----------------------')
lst=[22,33,44,55]
print(len(lst))
print(lst.__len__())
print(len(stu1))

