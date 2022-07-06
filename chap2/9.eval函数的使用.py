# coding:utf-8
# @Time : 2022/4/20 11:24 
# @Author : clf
# @File : 9.eval函数的使用.py.py 
# @Software: PyCharm
s='3.14+3'
print(s,type(s))
x = eval(s) #去掉引号，执行了加分运算
print(x,type(x))

#eval()与input()一起使用
# age=eval(input('请输入你的年龄：')) #将字符串转成了int类型，相当于int(age)
# print(age,type(age))
#
# height = eval(input('请输入你的身高：')) #将字符串转成了float类型，相当于float(age)
# print(height,type(height))
hello='Beijing'
print(hello)
#使用eval报错的情况
print(eval('hello')) #通过eval函数去掉引号，就变成了标识符，hello即变量名，如果前面不定义hello，则就会报错。
#NameError: name 'hello' is not defined