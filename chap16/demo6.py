# coding:utf-8
# @Time : 2022/6/30 15:35 
# @Author : clf
# @File : demo6.py.py 
# @Software: PyCharm

from multiprocessing import Process,Queue
import time

#向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = '消息'+str(i)
            q.put(message)
            print('写入：%s'%message)
#从队列读取数据
def read_task(q):
    time.sleep(1) #休眠1s
    while not q.empty():
        print('读取：%s'%q.get(True,2)) #等待2s，如果还没读出任何消息，则抛出Queue.empty异常

if __name__ == '__main__':
    print('------------父进程开始------------------')
    q=Queue() #父进程创建Queue，并传给各个子进程
    pw=Process(target=write_task,args=(q,))  #实例化写入队列的子进程，并且传递队列
    pr=Process(target=read_task,args=(q,))   #实例化读取队列的子进程，并且传递队列
    pw.start()  #启动进程，写入
    pr.start()  #启动进程，读取
    pw.join() #等待结束
    pr.join()
    print('---------------父进程结束-----------------')