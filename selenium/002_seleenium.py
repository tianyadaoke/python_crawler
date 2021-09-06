# coding: utf-8
# @Time: 2021/9/6 13:21
# @Author: Bing
# @File: 002_seleenium
# @Project: study
from selenium import webdriver
path='chromedriver.exe'
brower=webdriver.Chrome(path)

# 基本使用
# url="https://www.baidu.com"
# brower.get(url)

url='https://www.jd.com/?country=USA'
brower.get(url)

#page source获取网页源码
content=brower.page_source
print(content)