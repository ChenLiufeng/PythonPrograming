# coding:utf-8
# @Time : 2022/6/28 20:32 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm
import datetime
import time
def inputdate():
    indate=input('请输入开始日期：（20220628）后按回车：')
    indate=indate.strip() #如果出现空格的话，先去掉空格
    datestr=indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]
    return datetime.datetime.strptime(datestr,'%Y-%m-%d')

if __name__ == '__main__':
    print('--'*30)
    sdate=inputdate()
    in_num=int(input('请输入间隔天数：'))
    fdate=sdate+datetime.timedelta(days=in_num)
    print('您推算的日期是：'+str(fdate).split(' ')[0])