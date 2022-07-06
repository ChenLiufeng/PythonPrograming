# coding:utf-8
# @Time : 2022/6/14 20:56 
# @Author : clf
# @File : demo3.py.py 
# @Software: PyCharm
def fun(*args): #函数定义时的可变位置参数
    print(args)
fun(10)
fun(10,30)
fun(20,30,40) #返回结果是元组(20, 30, 40)

def fun1(**args): #个数可变的关键字形参，返回结果是一个字典
    print(args)

fun1(a=10)
fun1(a=10,b=20,c=30) #返回结果是{'a': 10, 'b': 20, 'c': 30}