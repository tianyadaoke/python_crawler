import requests
url='http://www.baidu.com'
response=requests.get(url)
#设置相应编码格式
response.encoding='utf-8'
#一个类型和六个属性
print(type(response))
#以字符串形式返回网页源码
print(response.text)
#返回一个url地址
print(response.url)
#返回二进制数据
print(response.content)
#返回响应状态码
print(response.status_code)
#返回响应头
print(response.headers)