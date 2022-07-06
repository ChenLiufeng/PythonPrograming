# coding:utf-8
# @Time : 2022/7/1 10:27 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm
'''
服务器向浏览器发送“hello world”
使用Socker模块，通过客户端浏览器向本地服务器（IP地址为127.0.0.1）发起请求
服务器接到请求，向浏览器发送“Hello World”
'''

import socket   #导入socket模块
host='127.0.0.1' #主机IP
port=8080   #端口号
web=socket.socket()  #创建socket对象
web.bind((host,port)) #绑定端口
web.listen(5)  #设置最多连接数
print('服务器等待客户端连接...')
while True:  #开启死循环
    conn,addr=web.accept()  #建立客户端连接
    data=conn.recv(1024)  #获取客户端请求数据
    print(data)   #打印接收到的数据
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World') #向客户端发送数据
    conn.close()  #关闭连接