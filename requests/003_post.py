import requests
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
data = {'kw': 'apple'}
response=requests.post(url=url,data=data,headers=headers)
content=response.text
print(content)
obj=json.loads(content)
print(obj)

#post不需要编解码
#请求参数是data
#不需要请求对象定制