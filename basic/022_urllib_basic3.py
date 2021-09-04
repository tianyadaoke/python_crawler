# coding: utf-8
# @Time: 2021/9/3 14:15
# @Author: Bing
# @File: 022_urllib_basic3
# @Project: basic
import urllib.request

url = "https://www.google.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
request=urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
