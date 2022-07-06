# coding:utf-8
# @Time : 2022/6/13 15:20 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm
scores={'Jack':29,'Mark':98,'Frank':90}
print(scores['Jack'])
# print(scores['Marry']) #KeyError: 'Marry'

print(scores.get('Frank'))
print(scores.get('Marry')) #None
print(scores.get('Marry',99)) #99是在查询‘Marry’所对的value不存在时返回，提供的一个默认值