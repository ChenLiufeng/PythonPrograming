# coding:gbk
# @Time : 2022/6/20 18:09 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm
'''
MyContentMgrʵ�������ⷽ�� __enter__(),__exit__()��Ϊ���������������Ĺ�����Э��
��������ʵ�����󣬳�Ϊ�����Ĺ�����
MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter����������ִ����')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit����������ִ����')
    def show(self):
        print('show����������ִ����')


with MyContentMgr() as file:
    file.show()

