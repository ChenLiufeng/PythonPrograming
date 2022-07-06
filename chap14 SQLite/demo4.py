# coding:utf-8
# @Time : 2022/6/29 13:54 
# @Author : clf
# @File : demo4.py.py 
# @Software: PyCharm
import sqlite3

#连接到SQLite数据库，数据库文件是mrsoft.db
conn=sqlite3.connect('mrsoft.db')
#创建一个Cursor
cursor=conn.cursor()
cursor.execute('delete from user where id=?',(1,))
cursor.execute('select * from user')
result=cursor.fetchall()
print(result)
#关闭游标
cursor.close()
conn.commit()
conn.close()