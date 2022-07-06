# coding:utf-8
# @Time : 2022/7/1 9:27 
# @Author : clf
# @File : demo11.py.py 
# @Software: PyCharm
'''
使用队列模拟生产者消费者模式
定义一个生产者类Productor，定义一个消费者类Consumer。
生产者生成5件产品，依次写入队列，
而消费者依次从队列中取出产品，代码如下：
'''

from queue import Queue
import random,threading,time

#定义生产者
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            print('生产者%s将产品%d加入队列！'%(self.getName(),i))
            self.data.put(i)
            time.sleep(random.random())
        print('生产者%s完成！'%self.getName())

#消费者类
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            val=self.data.get()
            print('消费者%s将产品%d从队列中取出！'%(self.getName(),val))
            time.sleep(random.random())
        print('消费者%s完成！'%self.getName())

if __name__ == '__main__':
    print('-------------主线程开始-------------------')
    queue=Queue()   #实例化队列
    produce=Producer('Producer',queue) #实例化线程Producer，并传入队列作为参数
    consumer=Consumer('Consumer',queue) #实例化线程Consumer，并传入队列作为参数
    produce.start()    #启动线程Producer
    consumer.start()   #启动线程Consumer
    produce.join()     #等待线程Producer结束
    consumer.join()    #等待线程Consumer结束
    print('------------主线程结束--------------')