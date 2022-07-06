# coding:utf-8
# @Time : 2022/6/28 16:59 
# @Author : clf
# @File : demo8.py.py 
# @Software: PyCharm
#coffee_name={'1':'蓝山','2':'卡布奇洛','3':'拿铁','4':'皇家咖啡','5':'女五咖啡','6':'美丽与哀愁'}
coffee_name=('蓝山','卡布奇洛','拿铁','皇家咖啡','女五咖啡','美丽与哀愁')
print('本店经营的咖啡有：')
for index,item in enumerate(coffee_name):
    print(index+1,'.',item,end=' ')
index=int(input('\n请输入您喜欢的咖啡编号：'))
if 0 <=index <= len(coffee_name):
    print(f'您的咖啡[{coffee_name[index-1]}]好了，请您慢用')