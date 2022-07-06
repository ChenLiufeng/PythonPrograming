# coding:utf-8
# @Time : 2022/4/20 16:13 
# @Author : clf
# @File : 4.嵌套if.py.py 
# @Software: PyCharm
answer = input('请问，您喝酒了吗？y/n')
if answer == 'y': #代表喝酒了
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('构不成酒驾，祝您一路平安')
    elif proof<80:
        print('已构成酒驾标准，请不要开车')
    else:
        print('已达到醉驾标准，请千万不要开车')

else:#代表没喝酒的情况
    print('您走吧，没您啥事儿！')