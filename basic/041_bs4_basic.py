# coding: utf-8
# @Time: 2021/9/5 23:35
# @Author: Bing
# @File: 041_bs4_basic
# @Project: basic
from bs4 import BeautifulSoup

# 解析本地文件
# 默认打开是gbk
soup = BeautifulSoup(open('041_bs4_basic.html', encoding='utf-8'), 'lxml')
# print(soup)
#找到第一个符合条件的数据
print(soup.a)
print(soup.a.attrs)
print('--------------------')
#find 返回第一个符合条件的数据
print(soup.find('a'))
print(soup.find('a',title='google'))
print(soup.find('a',class_='googleclass'))
print('--------------------')
# 返回列表，所有符合条件
print(soup.findAll('a'))
#获取多个符合条件数据列表
print(soup.findAll(['a','span']))
#limit限制前几个数据
print(soup.findAll('li',limit=2))
