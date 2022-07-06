# coding:utf-8
# @Time : 2022/6/28 17:57 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm
def show(lst):
     for item in lst:
          for i in item:
               print(i,end='\t\t')
          print()
lst=[['01','电风扇','美的',500],
     ['02','洗衣机','松下',3500],
     ['03','微波炉','老板',1500],
     ['04','空气炸锅','九阳',2000]]
print('编号\t\t名称\t\t\t品牌\t\t单价\t\t')
show(lst)
for item in lst:
     item[0]='0000'+item[0]
     item[3]='&{:.2f}'.format(item[3])
print('编号\t\t\t名称\t\t\t品牌\t\t单价\t\t')
show(lst)