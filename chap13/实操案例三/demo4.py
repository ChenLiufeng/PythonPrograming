# coding:utf-8
# @Time : 2022/6/28 14:39 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm
import random
price=random.randint(1000,1500)
print('今日竞猜商品为小米扫地机器人：价格在1000--15000之间：')
guess=int(input())
if guess>price:
    print('大了')
elif guess<price:
    print('小了')
else:
    print('猜对了')