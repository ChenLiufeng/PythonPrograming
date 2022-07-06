# coding:utf-8
# @Time : 2022/6/21 11:23 
# @Author : clf
# @File : demo8.py.py 
# @Software: PyCharm

import os.path
print(os.path.abspath('demo7.py')) #获取文件或目录的绝对路径
print(os.path.exists('demo9.py'),os.path.exists('demo10.py')) #判断文件或目录是否存在，存在返回True，否则返回False

print(os.path.join('E:\\Python','demo8.py')) #将目录与目录或者文件名拼接起来
print(os.path.split('E:\\Users\\Clf\\PYTHON_TEST\\chap11\\demo7.py')) #将目录与文件进行拆分
print(os.path.splitext('demo8.py')) #拆分文件与后缀名
print(os.path.basename('E:\\Users\\Clf\\PYTHON_TEST\\chap11\\demo7.py')) #从目录中提取文件名
print(os.path.dirname('E:\\Users\\Clf\\PYTHON_TEST\\chap11\\demo7.py')) #从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('E:\\Users\\Clf\\PYTHON_TEST\\chap11')) #判断是否为路径,如果存在返回True，否则返回false