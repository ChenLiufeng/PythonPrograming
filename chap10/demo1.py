# coding:utf-8
# @Time : 2022/6/15 19:53 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm

class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('汽车已启动')

car = Car('宝马X5')
car.start()
print(car.brand)