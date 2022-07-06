# coding:utf-8
# @Time : 2022/6/30 11:43 
# @Author : clf
# @File : demo3.py.py 
# @Software: PyCharm
from multiprocessing import Pool
import os,time

def task(name):
    print('子进程(%s)执行task %s...'%(os.getpid(),name))
    time.sleep(1)   #休眠1s

if __name__ == '__main__':
    print('父进程(%s).'%os.getpid())
    p=Pool(3) #定义一个进程池，最大进程数为3
    for i in range(10):  #从0到开始循环10次
        p.apply_async(task,args=(i,)) #使用非阻塞方式调用task()函数
    print('等待所有子进程结束....')
    p.close() #关闭进程池，关闭后p不再接收新的请求
    p.join()  #等待子进程结束
    print('所有子进程结束。')