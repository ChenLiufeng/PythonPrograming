# coding:gbk
# @Time : 2022/6/20 18:09 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm
'''
MyContentMgr实现了特殊方法 __enter__(),__exit__()称为对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器
MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
    def show(self):
        print('show方法被调用执行了')


with MyContentMgr() as file:
    file.show()

