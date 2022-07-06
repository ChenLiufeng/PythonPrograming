# coding:utf-8
# @Time : 2022/6/13 21:46 
# @Author : clf
# @File : demo7.py.py 
# @Software: PyCharm
s='hello,world'
'''判断是否是合法的标识符'''
print('1.',s.isidentifier()) #False
print('2.','hello'.isidentifier()) #True
print('3.','%123'.isidentifier()) #False
print('4.','张三'.isidentifier())  #True
'''判断'''

print('5.','\t'.isspace()) #True
print('6.','张三'.isalpha()) #True
print('7.','Hello'.isalpha()) #True
print('8.','hello&'.isidentifier()) #False
#判断是否是十进制数字
print('9.','123'.isdecimal()) #True
print('10.','123四'.isdecimal()) #False
print('11.','Ⅱ'.isdecimal()) #False

#判断是否是数字
print('12.','123'.isnumeric()) #True
print('13.','123四'.isnumeric()) #True
print('14.','Ⅱ'.isnumeric()) #True

print('15.','abc1'.isalnum()) #True
print('16.','张三1'.isalnum()) #True
print('17.','abc！'.isalnum()) #False