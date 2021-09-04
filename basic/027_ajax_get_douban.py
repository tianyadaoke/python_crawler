# coding: utf-8
# @Time: 2021/9/4 13:55
# @Author: Bing
# @File: 027_ajax_get_douban
# @Project: basic
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
req = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')
print(content)
fp = open('douban.json', 'w', encoding='utf-8')
fp.write(content)
