# coding:utf-8
# @Time : 2022/4/21 10:03 
# @Author : clf
# @File : 13.跳转语句continue-if.py.py 
# @Software: PyCharm
s = 0
for i in range(1,101):
    if i%2==1:
        continue
    s += i
print('1~100之间的偶数和：',s)
