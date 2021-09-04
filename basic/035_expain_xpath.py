# coding: utf-8
# @Time: 2021/9/4 23:36
# @Author: Bing
# @File: 035_expain_xpath
# @Project: basic
from lxml import etree

# xpath expain local file
tree = etree.parse('035_expain_xpath.html')
# print(tree)
# 查找孙节点li中带id的节点
# li_list=tree.xpath('//ul/li[@id]')

# 查找id为11的标签
# li_list=tree.xpath('//ul/li[@id=11]')
# print(len(li_list))

# 查找到id为11的标签的class属性值
# li=tree.xpath('//ul/li[@id=11]/@class')
# print(li)

# 查找id中包含l的li标签
li_list = tree.xpath('//ul/li[contains(@id,"l")]')
print(len(li_list))

# 查找id中l开头的标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list)