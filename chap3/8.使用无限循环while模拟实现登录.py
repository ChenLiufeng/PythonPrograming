# coding:utf-8
# @Time : 2022/4/20 17:05 
# @Author : clf
# @File : 8.使用无限循环while模拟实现登录.py.py 
# @Software: PyCharm
i=0 #统计循环执行的次数
while i<3: #0,1,2,当i=3时，循环执行结束
    user_name=input('请输入您的用户名：')
    pwd = input('请输入您的密码：')
    #判断
    if user_name=='clf' and pwd=='8888':
        print('系统正在登录，请稍后')
        #改变循环条件，退出循环
        i=8
    else:
        if i<2: #当只有0次机会的时候不打印
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i += 1  #改变循环变量
if i==3: #当用户名或密码输入不正确的时候，循环执行结束时，i的最大值为3
    print('对不起，三次均输入错误')
