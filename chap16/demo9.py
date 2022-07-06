# coding:utf-8
# @Time : 2022/6/30 14:21
# @Author : clf
# @File : demo4.py.py
# @Software: PyCharm

from threading import Thread
import time

def plus():
    print('--------子线程1开始-----------')
    global g_num
    g_num += 50
    print('g_num is %d'%g_num)
    print('--------子线程1结束-----------')

def minus():
    print('--------子线程2开始-----------')
    global g_num
    g_num -= 50
    print('g_num is %d'%g_num)
    print('--------子线程2结束-----------')

g_num=100 #定义一个全局变量
if __name__ == '__main__':
    print('-------主线程开始-----------')
    print('g_num is %d' % g_num)
    #实例化线程
    p1=Thread(target=plus)
    p2=Thread(target=minus)
    #开启线程
    p1.start()
    p2.start()
    #等待线程结束
    p1.join()
    p2.join()
    print('----------主线程结束--------------')
