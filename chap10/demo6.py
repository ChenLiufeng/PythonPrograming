# coding:utf-8
# @Time : 2022/6/15 21:52 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm
# print(dir(object))

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age=age
class D(A):
    pass
x=C('Jack',20) #x是C类型的一个实例对象
print(x.__dict__) #实例对象的属性字典
print(C.__dict__)

print(x.__class__) #<class '__main__.C'>输出对象所属的类
print(C.__bases__) #C类的父类类型的元素
print(C.__base__) #类的基类，离得最近的父类
print(C.__mro__) #类的层次结构(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__())#子类的列表