# coding: utf-8
# @Time: 2021/9/4 23:02
# @Author: Bing
# @File: 033_urllib_proxy
# @Project: basic
import urllib.request

url = "http://www.baidu.com/s?wd=ip"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}
proxies = {
    'http': '123.171.42.178:3256'
}

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
