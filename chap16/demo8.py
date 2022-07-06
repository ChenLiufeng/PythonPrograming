# coding:utf-8
# @Time : 2022/6/30 18:17 
# @Author : clf
# @File : demo8.py.py 
# @Software: PyCharm
import  threading
import time

class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg='子线程'+self.name+'执行,i='+str(i) #name属性中保存的是当前线程的名字
            print(msg)

if __name__ == '__main__':
    print('--------主程序开始-------------')
    #创建子线程
    t1=SubThread()
    t2=SubThread()
    #启动子线程
    t1.start()
    t2.start()
    #等待子进程
    t1.join()
    t2.join()
    print('--------主程序结束-------------')