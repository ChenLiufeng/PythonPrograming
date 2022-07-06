# coding:utf-8
# @Time : 2022/4/21 11:10 
# @Author : clf
# @File : 16.实战三九九乘方表.py.py 
# @Software: PyCharm
#输出九九乘方表
for i in range(1,10): #9行
    for j in range(1,i+1): #列
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print() #换行