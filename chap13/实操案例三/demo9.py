# coding:utf-8
# @Time : 2022/6/28 17:41 
# @Author : clf
# @File : demo9.py.py 
# @Software: PyCharm
scores =(('1',11),('2',22),('3',33),('4',44),('5',55))
for index,item in enumerate(scores):
    print(index+1,'.',end=' ')
    for score in item:
        print(score,end=' ')
    print()