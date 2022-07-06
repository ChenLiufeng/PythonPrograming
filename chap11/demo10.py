# coding:utf-8
# @Time : 2022/6/21 10:18 
# @Author : clf
# @File : demo10.py.py 
# @Software: PyCharm

with open('logo2018.png','rb') as src_file:
    with open('copy21logo.png','wb') as target_file:
      target_file.write(src_file.read())