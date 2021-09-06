# coding: utf-8
# @Time: 2021/9/6 12:57
# @Author: Bing
# @File: 042_bs4_starbucks
# @Project: basic
import urllib.request
from bs4 import BeautifulSoup
url='https://www.starbucks.com.cn/menu/'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
soup=BeautifulSoup(content,'lxml')
name_list=soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())