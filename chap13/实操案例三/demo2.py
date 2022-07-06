# coding:utf-8
# @Time : 2022/6/28 14:19 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm

print('用户手机账号原有话费金额为：\033[0;35m8元\033[m')
money=int(input('请输入用户充值金额：'))
money +=8
print('当前的余额为：\033[0:35m',money,'元\033[m')

num=int(input('请输入您当天行走的步数：'))
calorie=num*28
print(f'今天共消耗了卡路里{calorie},即{calorie/1000}千卡')