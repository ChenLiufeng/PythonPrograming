# coding:utf-8
# @Time : 2022/6/28 19:19 
# @Author : clf
# @File : demo2.py.py 
# @Software: PyCharm
import prettytable as pt #引入漂亮表格

#显示坐席
def show_ticket(row_nuw):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_nuw):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)
#订票
def order_tiket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5'] #创建表头
    for i in range(row_num):
        if int(row)==i+1:#如果订购的行为i+1
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票'] #先初始化所有数据为有票
            lst[int(column)]='已售' #对应输出的列标注为已售
            tb.add_row(lst) #再添加到表格中
        else:
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row_num=13
    show_ticket(row_num)
    choose_num=input('请输入选择的座位，如13,5表示13排5号座位')
    try:
        row,column=choose_num.split(',')
    except:
        print('输入格式有误，如13排5号座位，应该输入13,5')
    order_tiket(row_num,row,column)