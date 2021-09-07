# urllib vs #requests
# get请求
# post请求
# 代理
# cookie
# ajax

import requests

url = 'https://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
data = {'wd': '北京'}
response = requests.get(url=url, params=data, headers=headers)
print(response.text)
# 参数使用params传递
# 参数无需urlencode编码
# 无需请求对象定制
# 请求资源路径可以不加？

