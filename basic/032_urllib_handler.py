# coding: utf-8
# @Time: 2021/9/4 22:56
# @Author: Bing
# @File: 032_urllib_handler
# @Project: basic
import urllib.request

url = "http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}
request = urllib.request.Request(url=url, headers=headers)
# handler build_opener open
# get handler object
handler = urllib.request.HTTPHandler()
# get opener object
opener=urllib.request.build_opener(handler)
# call open method
response = opener.open(request)
content=response.read().decode('utf-8')
print(content)