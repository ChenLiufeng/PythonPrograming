# coding:utf-8
# @Time : 2022/6/24 11:08 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm
name1='林黛玉'
name2='薛宝钗'
name3='贾元春'
name4='贾探春'
name5='史湘云'
print('①',name1)
print('②',name2)
print('③',name3)
print('④',name4)
print('⑤',name5)
print('列表-----------------')
lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_no=['①','②','③','④','⑤']
for i in range(5):
    print(lst_no[i],lst_name[i])
print('zip------------------------')
for s,name in zip(lst_no,lst_name):
    print(s,name)

print('字典----------------------')
d={'①':'林黛玉','②':'薛宝钗','③':'贾元春','④':'贾探春','⑤':'史湘云'}
for key in d:
    print(key,d[key])
