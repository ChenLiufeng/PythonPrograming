# coding:utf-8
# @Time : 2022/6/28 15:09 
# @Author : clf
# @File : demo5.py.py 
# @Software: PyCharm
for i in range(1,4):
    username=input('请输入用户名：')
    pwd=input('请输入密码：')
    if username=='admin'and pwd=='8888':
        print('登录成功！')
        break
    else:
        print('用户名或密码不正确')
        if i<3:
            print(f'您还有{3-i}次机会！！！')
else:
    print('对不起，三次均输入错误，请联系管理员')