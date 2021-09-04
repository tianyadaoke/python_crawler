# coding: utf-8
# @Time: 2021/9/3 13:30
# @Author: Bing
# @File: 016_file
# @Project: basic
# f=open('test.txt','w')
# a模式为追加
# f=open('test.txt','a')
# f.write('hello file\n'*5)
# f.close()

f=open('test.txt','r')
content = f.read()
print(content)
f.close()


f=open('test.txt','r')
content = f.readline()
print(content)
f.close()


f=open('test.txt','r')
content = f.readlines()
print(content)
f.close()