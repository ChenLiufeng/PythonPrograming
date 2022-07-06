# coding:utf-8
# @Time : 2022/6/14 21:22 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm

def fun(a,b=10): #b是在函数定义处，所以b为形参，进行了赋值，b为默认值形参
    print('a=',a)
    print('b=',b)

def fun2(*args): #个数可变的位置形参
    print(args)

def fun3(**args2): #个数可变的关键字形参
    print(args2)

fun2(10,20,30,40)
fun3(a=10,b=22,c=33,d=44,e=55)

def fun4(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)