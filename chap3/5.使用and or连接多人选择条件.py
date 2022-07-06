# coding:utf-8
# @Time : 2022/4/20 16:21 
# @Author : clf
# @File : 5.使用and or连接多人选择条件.py.py 
# @Software: PyCharm
user_name = input('请输入您的用户名：')
pwd = input('请输入您的密码：')
if user_name=='clf' and pwd=='888888':
    print('登录成功')
else:
    print('用户名或密码不正确')