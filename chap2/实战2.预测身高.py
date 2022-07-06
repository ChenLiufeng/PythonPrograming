# coding:utf-8
# @Time : 2022/4/20 15:13 
# @Author : clf
# @File : 实战2.预测身高.py.py 
# @Software: PyCharm
'''
题目：根据父母的身高预测儿子的身高
需求：从键盘输入父母的身高，并使用eval()转换float格式，计算公式：儿子身高=（父亲身高+母亲身高）*0.54
'''

father_height = eval(input('请输入父亲的身高：'))
mother_height = eval(input('请输入母亲的身高：'))
son_height = (father_height + m0ther_height)*0.54
print('预测儿子的身高为：',round(son_height,3))