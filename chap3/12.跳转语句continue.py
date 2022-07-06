# coding:utf-8
# @Time : 2022/4/21 9:56 
# @Author : clf
# @File : 12.跳转语句continue.py.py 
# @Software: PyCharm
s = 0
i = 1
while i<=100:
    if i%2==1:
        i += 1
        continue
    s += i
    i += 1
print('1~100之间的偶数和：',s)
