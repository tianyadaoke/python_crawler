# coding: utf-8
# @Time: 2021/9/5 17:19
# @Author: Bing
# @File: 037_xpath_parse_baidu
# @Project: basic

# 1.获取网页源码
import urllib.request

url = "https://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
# 2.解析服务响应的文件
from lxml import etree

tree = etree.HTML(content)
# xpath的返回值是一个列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')[0]
# 3.打印
print(result)
