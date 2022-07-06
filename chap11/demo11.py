# coding:utf-8
# @Time : 2022/6/21 11:45 
# @Author : clf
# @File : demo11.py.py 
# @Software: PyCharm

import os
path=os.getcwd() #得到当前目录路径
lst_files=os.walk(path) #遍历所有的文件
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('--------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('-----------------------')