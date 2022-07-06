# coding:utf-8
# @Time : 2022/4/20 16:07 
# @Author : clf
# @File : 3.多重if.py.py 
# @Software: PyCharm
score = eval(input('请输入您的成绩：'))
#判断
if score<0 or score>=100:
    print('成绩有误')
elif 0 <= score<60:
    print('E')
elif 60 <= score<70:
    print('D')
elif 70 <= score<80:
    print('C')
elif 80 <= score<90:
    print('B')
else:
    print('A')