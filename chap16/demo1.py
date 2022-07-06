# coding:utf-8
# @Time : 2022/6/29 19:57 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm
from multiprocessing import Process #导入模块

#执行子进程代码
def test(interval):
    print('我是子进程')
#执行主程序
def main():
    print('主程序开始')
    p=Process(target=test,args=(1,))#实例化Process进程类
    p.start()
    print('主程序结束')
if __name__ == '__main__':
    main()
