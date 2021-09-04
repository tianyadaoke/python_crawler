# coding: utf-8
# @Time: 2021/9/4 17:17
# @Author: Bing
# @File: 030_urllib_exception
# @Project: basic
# 'https://blog.csdn.net/u011008029/article/details/51315339'
import urllib.request
import urllib.error
url='https://goudan11111xxeror/article/details/51315339error'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}
try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print('url不存在')
