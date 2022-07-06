# coding:utf-8
# @Time : 2022/6/28 17:52 
# @Author : clf
# @File : demo1.py.py 
# @Software: PyCharm

def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count += 1
    return count
if __name__ == '__main__':
    s='hellopython,hellojav,hellogo'
    ch=input('请输入要统计的字符：')
    count=get_count(s,ch)
    print('出现的次数',count)