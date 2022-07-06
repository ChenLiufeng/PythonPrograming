# coding:utf-8
# @Time : 2022/4/20 17:23 
# @Author : clf
# @File : 9.嵌套结构循环.py.py 
# @Software: PyCharm
#三行四列
print('---------输出三行四列-----------')
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    #换行
    print()
#输出一个直角三角形
print('----------输出一个直角三角形----------------')
for i in range(1,6):
    for j in range(1,i+1): #*的个数与行数相同，range(1,2),range(1,3)1,2,3
        print('*',end='')
    #换行
    print()
#输出一个倒直三角形
print('---------输出一个倒直三角形-----------')
for i in range(1,6):
    for j in range(1,7-i):
        print('*', end='')
        # 换行
    print()
#输出一个等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
print('------输出一个等腰三角形--------------')
for i in range(1,6):
    #输出倒三角形
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
        # 换行
    print()
#输出一个菱形
print('-------输出一个菱形-------------')
row=eval(input('请输入菱形的行数：'))
top_row =(row+1)//2 #上增部分的行数
#菱形的上半部分
for i in range(1,top_row + 1):
    #输出倒三角形
    for j in range(1,top_row-i+1):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
        # 换行
    print()
#菱形的下半部分
bottom_row = row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ', end='')
    #倒三角形 range(1,8)
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')#不换行
    print() #换行

#输出一个空菱形
print('-------输出一个空菱形-------------')
row=eval(input('请输入菱形的行数：'))
while row%2==0:
    print('重新输入菱形的行数：')
    row = eval(input('请输入菱形的行数：'))
top_row =(row+1)//2 #上增部分的行数
#菱形的上半部分
for i in range(1,top_row + 1):
    #输出倒三角形
    for j in range(1,top_row-i+1):
        print(' ',end='')
    for k in range(1,i*2):
        if k == 1 or k == i * 2 - 1:
            print('*',end='')
        else:
            print(' ', end='')
        # 换行
    print()
#菱形的下半部分
bottom_row = row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ', end='')
    #倒三角形 range(1,8)
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')#不换行
        else:
            print(' ', end='')
    print() #换行


