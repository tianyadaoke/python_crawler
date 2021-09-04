# coding: utf-8
# @Time: 2021/9/3 22:57
# @Author: Bing
# @File: 025_post
# @Project: basic
# Request URL: https://www.google.com/async/translate?vet=12ahUKEwiZruCz2OPyAhXIRkEAHdZiDPcQqDh6BAgCECY..i&ei=2osyYZnZA8iNhbIP1sWxuA8&yv=3

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
data = {
    'kw': 'apple'
}
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
obj = json.loads(content)
print(obj)