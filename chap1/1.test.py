#conding:utf-8
'''
题目:输出自我介绍
需求：使用input()函数从键盘输入姓名、年龄，座右铭，并使用print()函数输出到控制台
'''
#键盘输入
name = input('请输入您的姓名：')  #从键盘输入姓名
age = int(input('请输入您的年龄：'))  #从键盘输入年龄
motto = input('请输入您的座右铭：') #从键盘输入座右铭
print('--------自我介绍--------------')
#打印结果
print('姓名：', name)
print('年龄：',age)
print('座右铭：',motto)