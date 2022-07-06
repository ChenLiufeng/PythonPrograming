# coding:gbk
# @Time : 2022/6/20 17:41 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm

scr_file=open('logo2018.png','rb')

target_file=open('copylogo.png','wb')

target_file.write(scr_file.read())

target_file.close()
scr_file.close()
