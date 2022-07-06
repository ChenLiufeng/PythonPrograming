# coding:utf-8
# @Time : 2022/4/21 9:11 
# @Author : clf
# @File : 10.跳转语句break.py.py 
# @Software: PyCharm
#计算累加和
sum = 0 #用于存储累加和
i = 1 #1.初始化变量
while i<=100: #2.条件判断
    sum += i  #3.语句块
    if sum > 20:
        print('累加和大于20的当前数',i)
        break
    i+=1 #4.改变变量
# print('1~100 之间的累加和为：',sum)

i = 0
while i<3:
    user_name = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    if user_name == 'clf' and pwd == 8888:
        print('系统正在登录，请稍后……')
        break
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
        i += 1
else:
    print('三次均输入错误')