fp=open('note.txt','w') #打开文件，w-write
print('武汉欢迎您！！！',file=fp) #输出到文件中
fp.close() #关闭文件

