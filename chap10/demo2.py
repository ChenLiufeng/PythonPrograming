# coding:utf-8
# @Time : 2022/6/15 19:56 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #年龄不希望在类的外部被使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外使用name和age
print(stu.name)
print(stu._Student__age)
