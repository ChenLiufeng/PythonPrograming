# coding:utf-8
# @Time : 2022/4/20 16:27 
# @Author : clf
# @File : 6.遍历循环.py.py 
# @Software: PyCharm
#遍历字符串
for i in 'hello':
    print(i)

#range()函数，产生一个[n,m)的整数序列，包含n，不包含m
for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i)
#计算累加和
sum = 0 #用于存储累加和
for i in range(1,11):
    sum += i
print('1~10之间的累加和为：',sum)

#100——999之间计算水仙花数
'''
153
3*3*3+5*5*5+1*1*1=153
'''
print('-----------100——999之间的水仙花数------------')
for i in range(100,1000):
    sd=i%10 #获得个位上的数字
    tens = i//10%10 #获得十位上的数字
    hundred = i//100 #百位数的数字
    if hundred**3+tens**3+sd**3==i:
        print(i,'为水仙花数')
