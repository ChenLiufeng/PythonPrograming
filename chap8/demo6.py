# coding:utf-8
# @Time : 2022/6/15 13:27 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm

def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1)
        return res
print(fac(6))