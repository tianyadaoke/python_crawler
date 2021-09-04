# coding: utf-8
# @Time: 2021/9/4 23:19
# @Author: Bing
# @File: 034_urllib_proxy_pool
# @Project: basic
import random
import urllib.request
proxies_pool = [{'http': '182.84.145.167:3256'},
                {'http': '27.191.60.232:3256'},
                {'http': '125.87.95.80:3256'},
                {'http': '163.125.29.74:8118'}]

proxies = random.choice(proxies_pool)
print(proxies)

url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}
request=urllib.request.Request(url=url,headers=headers)
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)