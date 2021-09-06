# coding: utf-8
# @Time: 2021/9/6 13:10
# @Author: Bing
# @File: 001_selenium_basic_jingdong
# @Project: study
import  urllib.request
url='https://www.jd.com'
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
#不能找到京东seckill
print(content)