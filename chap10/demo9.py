# coding:utf-8
# @Time : 2022/6/16 11:44 
# @Author : clf
# @File : demo9.py.py 
# @Software: PyCharm


class CPU:
    pass
class Disk:
    pass
class Comptuter:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

#浅拷贝
print('-------------------')
disk=Disk() #创建一个硬盘类的对象
computer=Comptuter(cpu1,disk)
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)