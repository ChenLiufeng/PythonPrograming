# coding:utf-8
# @Time : 2022/6/28 15:15 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm

import random

rand=random.randint(1,100)
for i in range(1,11):
    num=int(input('在我心中有个数1-100，请你猜一猜'))
    if num<rand:
        print('小了')
    elif num>rand:
        print('大了')
    else:
        print('恭喜你猜对了')
        break
print(f'您一共猜了{i}次')
if i<3:
    print('真聪明')
elif i<=7:
    print('还行')
else:
    print('out!!!')