# coding:utf-8
# @Time : 2022/6/15 13:47 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm
'''
查询某个演员出演了哪个作品
思路：
    1）先找到演员所在的行列
    2）再找演员对应的作品
'''
lst=[{'rating':[9.7,2062397],'id':1292052,'type':['犯罪','剧情'],
      'title':'肖申克的救赎','actors':['蒂姆.罗宾斯','摩根.弗里曼']},
      {'rating':[9.6,1562397],'id':1291552,'type':['剧情','爱情','同性'],
      'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
     {'rating': [9.5, 1522397], 'id': 1291852, 'type': ['爱情', '剧情'],
      'title': '阿甘正传', 'actors': ['汤姆.汉克斯', '罗宾.怀特']},
     ]

name=input('请输入你要查询的演员：')
for item in lst: #遍历列表 item是一个又一个字典
    act_lst=item['actors']
    # print(act_lst)
    for actors in act_lst: #遍历演员列表
        if name in actors:
            print(name, '出演了', item['title'])
    # for movie in item:  #遍历字典，得到movie，是一个字典中的key
    #     print(movie)
    # print('----------------------')
    #     # actors = movie['actors']
        # print(actors)
        # if name in actors:
        #     print(name,'出演了',item['title'])
