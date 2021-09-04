# coding: utf-8
# @Time: 2021/9/3 14:01
# @Author: Bing
# @File: 019_urllib_basic
# @Project: basic

import urllib.request
url="https://www.baidu.com"
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)
