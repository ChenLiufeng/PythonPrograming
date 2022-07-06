# coding:utf-8
# @Time : 2022/4/20 16:55 
# @Author : clf
# @File : 7.无线循环while.py.py 
# @Software: PyCharm

#4步执行法
#1.初始化变量
answer = input('今天上课了吗？y/n')
while answer=='y': #2.条件判断
    print('好好学习，天天向上') #3.语句块
    #4.改变变量
    answer = input('今天要上课吗？y/n')

#计算累加和
sum = 0 #用于存储累加和
i = 1 #1.初始化变量
while i<=100: #2.条件判断
    sum += i  #3.语句块
    i+=1 #4.改变变量
print('1~100 之间的累加和为：',sum)