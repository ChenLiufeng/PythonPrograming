# coding:utf-8
# @Time : 2022/6/15 20:05 
# @Author : clf
# @File : demo3.py.py 
# @Software: PyCharm

class Person(object):#Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear

stu=Student('张三',20,'1001')
teacher = Teacher('李四',34,10)
print(dir(Student))
stu.info()
teacher.info()
