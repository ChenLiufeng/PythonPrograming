# coding:utf-8
# @Time : 2022/6/30 18:32 
# @Author : clf
# @File : demo10.py.py 
# @Software: PyCharm
'''
使用互斥锁实现多人同时订购电影票功能
电影院某个场次只有100张电影票，10个用户同时抢购该电影票，
每售出一张，显示一次剩余电影票张数，
使用多线程和互斥锁模拟该过程
'''

from threading import Thread,Lock
import time

n=100  #共100张票
def task():
    global n
    mutex.acquire()    #上锁
    temp=n    #赋值给临时变量
    time.sleep(0.1) #休眠0.1s
    n=temp-1  #数量减1
    print('购买成功，剩余%d张电影票'%n)
    mutex.release() #释放锁

if __name__ == '__main__':
    mutex=Lock()  #实例化Lock类
    t_l=[]  #初始化一个列表
    for i in range(10):
        t=Thread(target=task) #实例化线程类
        t_l.append(t) #将线程存入到列表中
        t.start()  #启动线程
    for t in t_l:
        t.join() #等待子线程结束