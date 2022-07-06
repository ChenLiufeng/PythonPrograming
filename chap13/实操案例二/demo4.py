# coding:utf-8
# @Time : 2022/6/27 16:23 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm
height=int(input('请输入您的身高：'))
weight=int(input('请输入您的体重：'))
bmi=weight/(height+weight)
print('您的BMI的指数是：{:0.2f}'.format(bmi))