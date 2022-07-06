# coding:utf-8
# @Time : 2022/4/20 15:38 
# @Author : clf
# @File : 2.选择结构.py.py 
# @Software: PyCharm
number = eval(input('请输入您的6位中奖号码：'))

if number == 987654:
    print('恭喜您，中奖了')
else:
    print('您未中本期大奖')

#number=987654为true时，将“'恭喜您，中奖了'”赋值给变量result，否则将'您未中本期大奖'赋值为变量result

result='恭喜您，中奖了' if number==987654 else '您未中本期大奖'
print(result)