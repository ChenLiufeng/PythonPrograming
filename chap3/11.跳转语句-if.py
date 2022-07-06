# coding:utf-8
# @Time : 2022/4/21 9:46 
# @Author : clf
# @File : 11.跳转语句-if.py.py 
# @Software: PyCharm
for i in range(3):
    user_name = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    if user_name == 'clf' and pwd == '8888':
        print('系统正在登录，请稍后……')
        break #直接退出循环
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
else:
    print('三次均输入错误')