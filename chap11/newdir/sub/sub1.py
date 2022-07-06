# coding:utf-8
# @Time : 2022/6/21 11:41 
# @Author : clf
# @File : sub1.py.py 
# @Software: PyCharm

import os
path=os.getcwd() #得到当前目录路径
lst_files=os.walk(path) #遍历所有的文件
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)