# coding:utf-8
# @Time : 2022/6/23 16:05 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm

'''
一、使用print方式进行输出，输出的目的地是文件
'''
fp=open('e:/test.txt','w') #w表示只写 a+表示读写模式
print('奋斗成就更好的自己',file=fp)
fp.close()

'''
一、使用文件读取操作
'''
with open('e:/test1.txt','w') as file:
    file.write('奋斗成就更好的自己')