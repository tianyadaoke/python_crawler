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
# 找到第一个符合条件的数据
print(soup.a)
print(soup.a.attrs)
print('--------------------')
# find 返回第一个符合条件的数据
print(soup.find('a'))
print(soup.find('a', title='google'))
print(soup.find('a', class_='googleclass'))
print('--------------------')
# 返回列表，所有符合条件
print(soup.findAll('a'))
# 获取多个符合条件数据列表
print(soup.findAll(['a', 'span']))
# limit限制前几个数据
print(soup.findAll('li', limit=2))
print('--------------------')
# 推荐select
# 返回多个数据列表
print(soup.select('a'))
# 类选择器
print(soup.select('.googleclass'))
# id选择器
print(soup.select('#baidu'))
# 属性选择器
# 查找li标签中有id的标签
print(soup.select('li[id]'))
print(soup.select('li[id="lisi"]'))
print('--------------------')
#层级选择器
print(soup.select('ul a'))
print(soup.select('ul>li'))
print(soup.select('li,a'))
print('--------------------')
#节点信息
obj=soup.select("#baidu")[0]
print(obj.string)
#推荐get_text()
print(obj.get_text())
#标签名字
print(obj.name)
print(obj.attrs)