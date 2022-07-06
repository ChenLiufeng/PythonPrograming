# coding:utf-8
# @Time : 2022/6/30 14:21 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm

from multiprocessing import Process

def plus():
    print('--------子进程1开始-----------')
    global g_num
    g_num += 50
    print('g_num is %d'%g_num)
    print('--------子进程1结束-----------')

def minus():
    print('--------子进程2开始-----------')
    global g_num
    g_num - 50
    print('g_num is %d'%g_num)
    print('--------子进程2结束-----------')

g_num=100 #定义一个全局变量
if __name__ == '__main__':
    print('-------主程序开始-----------')
    print('g_num is %d' % g_num)
    #实例化进程
    p1=Process(target=plus)
    p2=Process(target=minus)
    #开启进程
    p1.start()
    p2.start()
    #等待进程结束
    p1.join()
    p2.join()
    print('----------主程序结束--------------')