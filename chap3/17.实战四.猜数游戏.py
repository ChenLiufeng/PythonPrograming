# coding:utf-8
# @Time : 2022/4/21 11:28 
# @Author : clf
# @File : 17.实战四.猜数游戏.py.py 
# @Software: PyCharm
import random
rand = random.randint(1,100)#random内置函数，随机生成1——100以内的整数
count = 1 #记录猜的次数
while count <= 10: #只有10次机会
    number = eval(input('在我心中有个数，1-100之间，请你猜一猜：'))
    if number == rand: #如果猜的数相等
        print('猜对了')
        break #退出游戏
    elif number > rand: #猜大了
        print('大了')
    else:
        print('小了') #猜小了
    count += 1
if count<=3:
    print('你真聪明，一共猜了',count,'次')
elif count <= 6:
    print('还可以，一共猜了', count, '次')
else:
    print('猜的次数有点多，一共猜了', count, '次')