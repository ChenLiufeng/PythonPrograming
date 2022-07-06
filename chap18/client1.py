# coding:utf-8
# @Time : 2022/7/1 10:59
# @Author : clf
# @File : client.py.py
# @Software: PyCharm
import socket  #导入socket模块
s=socket.socket() #创建TCP/IP套接字
host=socket.gethostname() #获取主机地址
port=12345  #设置端口号
s.connect((host,port)) #主动初始化TCP服务器连接
print('已连接')
info=''
while info=='byebye':
    send_data=input('请输入要发送的数据：') #提示用户输入数据
    s.send(send_data.encode())  #发送TCP数据
    #接收对方发送过来的数据，最大接收1024个字节
recvData=s.recv(1024).decode()
print('接收到的数据为：',recvData)
#关闭套接字
s.close()

#E:\Users\Clf\PYTHON_TEST\chap18\client.py