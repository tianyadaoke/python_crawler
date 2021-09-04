# coding: utf-8
# @Time: 2021/9/4 17:33
# @Author: Bing
# @File: 031_urllib_weibo
# @Project: basic
# https://weibo.com/6168974828/info

import urllib.request

url = 'https://weibo.com/6168974828/info'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 ',
    'cookie': 'UOR=www.google.com,weibo.com,www.google.com; _ga=GA1.2.2146693699.1629989962; SINAGLOBAL=3015163697805.2876.1629989965035; login_sid_t=b0a72925478e2d32fb8a1f61846c6abf; cross_origin_proto=SSL; _s_tentry=www.google.com; Apache=5022644862710.877.1630769179754; ULV=1630769179764:3:1:2:5022644862710.877.1630769179754:1630233740913; wb_view_log=1536*8641.25; SUB=_2A25MN-F8DeThGeBP7VoY9yrEyTSIHXVvRVW0rDV8PUNbmtAfLXfXkW9NRSVRtkePid_lpG3-gnQHz76r6wq_qfKt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.drEoRD7JuICS1W6kK0iN5JpX5KzhUgL.FoqpSon4S0BReon2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMceKqR1KMX1hzR; ALF=1662305450; SSOLoginState=1630769452; wvr=6; wb_view_log_6168974828=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1630770315160%2C%22dm_pub_total%22%3A7%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A26%2C%22msgbox%22%3A0%7D',
    'referer': 'https://weibo.com/6168974828/info'

}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
