# coding:utf-8
# @Time : 2022/6/29 11:04
# @Author : clf
# @File : demo1.py.py
# @Software: PyCharm
import sqlite3
#连接到SQLite数据库
#数据库文件是mrsoft.db,如果文件不存在，会自动在当前目录创建
conn=sqlite3.connect('mrsoft.db')
#创建一个Cursor
cursor=conn.cursor()
#执行一条SQL语句，创建user表
# cursor.execute('create table user(id int(10) primary key,name varchar(20))')
#
# #执行一条SQL语句，插入一条记录
# cursor.execute('insert into user(id,name) values("1","MRSOFT")')
# cursor.execute('insert into user(id,name) values("2","Andy")')
# cursor.execute('insert into user(id,name) values("3","明日科技小助手")')

#执行查询结果
cursor.execute('select * from user where id > ?',(1,))
#获取查询语句
# result1 = cursor.fetchone()
# print(result1)

result2=cursor.fetchall()
print(result2)
# result3=cursor.fetchmany(2)
# print(result3)
#关闭游标
cursor.close()
conn.commit() #提交事务
#关闭Connection
conn.close()