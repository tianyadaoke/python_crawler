# coding: utf-8
# @Time: 2021/9/3 14:01
# @Author: Bing
# @File: 019_urllib_basic
# @Project: basic

import urllib.request
url="https://www.baidu.com"
response = urllib.request.urlopen(url)
# 一个个字节读取
# content = response.read().decode('utf-8')
# print(content)

#读取几个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 读取所有行
# content = response.readlines()
# print(content)

# 返回状态码
print(response.getcode())
# 返回url
print(response.geturl())
# 返回header
print(response.getheaders())