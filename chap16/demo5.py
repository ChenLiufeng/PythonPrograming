# coding:utf-8
# @Time : 2022/6/30 15:20 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm
from multiprocessing import Queue

if __name__ == '__main__':
    q=Queue(3) #初始化一个Queue对象，最多可接收3条put消息
    q.put('消息1') #将消息写入队列中
    q.put('消息2')
    print(q.full()) #返回False
    q.put('消息3')
    print(q.full()) #返回True

    #因为消息队列已满，下面的try都会抛出异常
    #第一个try会等待2s后再抛出异常，第二个try会立刻抛出异常
    try:
        q.put('消息4',True,2)
    except:
        print('消息队列已满，现有消息数量：%s'%q.qsize()) #返回当前队列包含的消息数量

    try:
        q.put_nowait('消息4') #没有空间可写入
    except:
        print('消息队列已满，现有消息数量：%s'%q.qsize()) #返回当前队列包含的消息数量

    #读取消息时，先判断消息队列是否为空，再读取
    if not q.empty():
        print('---------从队列中获取消息---------')
        for i in range(q.qsize()):
            print(q.get_nowait())
    #先判断消息队列是否已满，再写入
    if not q.full():
        q.put_nowait('消息4')