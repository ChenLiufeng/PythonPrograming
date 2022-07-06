# coding:utf-8
# @Time : 2022/6/21 11:36 
# @Author : clf
# @File : demo9.py.py 
# @Software: PyCharm
'''
列出指定目录下的所有py文件
'''

import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)