# coding:utf-8
# @Time : 2022/6/15 13:41 
# @Author : clf
# @File : demo7.py.py 
# @Software: PyCharm
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))
print('---------------------')
for i in range(1,7):
    print(fib(i))