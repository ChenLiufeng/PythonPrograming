# coding:utf-8
# @Time : 2022/4/20 14:58 
# @Author : clf
# @File : 实战1：输出4位整数.py.py 
# @Software: PyCharm
'''
题目：从键盘获取一个四位整数，分别输入个位、十位、百位、千位上的数字
eval()
input()
'''
num=eval(input('请输入一个四位整数：'))
thousands = num//1000  #千位上的数字
hundred = num//100%10  #百位
tens = num//10%10 #十位
sd = num%10  #个位
print('个位数：',sd)
print('十位数：',tens)
print('百位数：',hundred )
print('千位数：',thousands)