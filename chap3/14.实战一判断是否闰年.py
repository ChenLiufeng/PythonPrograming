# coding:utf-8
# @Time : 2022/4/21 10:24 
# @Author : clf
# @File : 14.实战一判断是否闰年.py.py 
# @Software: PyCharm
'''
题目：输入一个年份，判断是否是闰年
需求：从键盘获取一个四位的整数年份，判断其是否为闰年
闰年判断条件为：能被4整除，但不能被100整除，或者能被400整除
'''
year = eval(input('请输入一个四位的年份')) #键盘输入年份，并转换为int格式
if (year%400==0 and year%100 !=0) or (year%400==0)  :
    print(year,'年是闰年')
else:
    print(year,'年是平年')