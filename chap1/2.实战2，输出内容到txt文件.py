#coding:utf-8
#输出“人生苦短，我用python”到文件text.txt

fp = open('text.txt','w')
print('人生苦短，我用python',file=fp)
fp.close()