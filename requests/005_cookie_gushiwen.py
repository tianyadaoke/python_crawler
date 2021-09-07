# 通过登录 绕过验证码
# __VIEWSTATE: uYMxy8asyM0+2g/N6Fj15YxCoupw/Fu1PlL5RZMOfRTJ+jpMEcjesyHOewDk0h4EQnGAgkrgChmBglVhOvt+pYdG/gGQiYeFd+QztPnovy5LzgREn9t6+ABAJy8=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 595165358@qq.com
# pwd: action
# code: 1GXV
# denglu: 登录
#__VIEWSTATEGENERATOR 和__VIEWSTATE都在源码的input隐藏中
import requests
#登录页面的url地址
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
content=response.text
# print(content)
# 解析源码
from bs4 import BeautifulSoup
soup=BeautifulSoup(content,'lxml')
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstategenerator,viewstate)
# 获取验证码图片
code=soup.select('#imgCode')[0].attrs.get('src')
code_url='https://so.gushiwen.cn'+code
# print(code_url)

# 获取图片之后下载到本地观察验证码，然后在控制台输入验证码，控制台输入它
# import urllib.request
# 有坑，不是同一个验证码
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')
#requests有一个方法session() 通过session返回值 就能使请求变成一个对象
session=requests.session()
response_code=session.get(code_url)
#注意此时要使用二进制数据，用于图片下载
content_code=response_code.content
with open('code.jpg','wb') as fp:
    fp.write(content_code)
code_name=input('请输入验证码')


# 点击登录
url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data={
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': code_name,
    'denglu': '登录'
}
response=session.post(url=url,headers=headers,data=data)
content=response.text
with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content)

# 两个难点，一个是隐藏域，一个是session