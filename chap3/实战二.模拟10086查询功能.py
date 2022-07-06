# coding:utf-8
# @Time : 2022/4/21 10:40 
# @Author : clf
# @File : 实战二.模拟10086查询功能.py.py 
# @Software: PyCharm
'''
题目：模拟10086查询功能
需求：
    输入1，显示当前余额；
    输入2，显示当前的剩余流量，单位为G
    输入3，显示当前的剩余通话，单位为分钟；
    输入0，退出自助查询系统
'''
#（1）初始化变量
flag = 'y'
#（2）条件判断
while flag=='y' :
    print('-----------------欢迎使用10086查询功能-------------------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话时长')
    print('0.退出系统')
    num = eval(input('请输入您要执行的操作'))
    if num==1:
        print('当前余额为234.5元')
    elif num==2:
        print('当前剩余流量为4GB')
    elif num == 3:
        print('当前剩余通话时长为200分钟')
    elif num == 0:
        print('程序退出，谢谢您的使用')
        break
    else:
        print('对不起，您输入的有误，请重新输入')
    #（4）改变变量
    flag = input('还要继续操作吗？y/n')
else:
    print('程序退出，谢谢您的使用')

