import requests

url = 'https://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
params = {
    'wd': 'ip'
}
proxy={
    'http':'183.240.203.136:8118'
}
response = requests.get(url=url, params=params, headers=headers,proxies=proxy)
content = response.text
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
