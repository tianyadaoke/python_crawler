# coding: utf-8
# @Time: 2021/9/5 23:16
# @Author: Bing
# @File: 040_jsonpath_taopiaopiao
# @Project: basic

import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1630876760939_135&jsoncallback=jsonp136&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'cookie': 'thw=xx; cna=bGmpGfg42RcCAbwaxco6zYTU; _ga=GA1.2.1108007909.1629842286; t=15dbd1cf230a1ce71cb339cdbbee3f7f; _ga_YFVFB9JLVB=GS1.1.1629842286.1.1.1629842319.0; sgcookie=E100HG8QkS%2Bo7%2FGV%2BgJY4Q%2FyFScUIM%2FbmXuoa0G13oSfTXlOCAeH%2FF3nPx%2Bzxo0zxdMEuaEEMYGPvXEBvu1Tjm2%2BBoXGrM5elLH2q%2Fp%2FbtrZCKc%3D; uc3=vt3=F8dCujHovPrcEWW6WyE%3D&id2=UUkNZKHFJrUrIw%3D%3D&nk2=AQrwus41&lg2=UtASsssmOIJ0bQ%3D%3D; lgc=bngfbi; uc4=id4=0%40U2uBb%2BLvb1G3akMRMSbpTzTnj4Cl&nk4=0%40A6eoVd79OJHwzQGTKUZlPJM%3D; tracknick=bngfbi; _cc_=UtASsssmfA%3D%3D; enc=iwsc7aNuXvz3%2Bzy9UtXnkp6YZnIo3tu8oj1%2F%2F%2FgOlARdt8KIcIDzMXARWfqMuUyJ8anzVIYztPZPPTvrJlvdhw%3D%3D; hng=GLOBAL%7Czh-CN%7CUSD%7C999; xlly_s=1; mt=ci=-1_0; cookie2=20c67ffe062979aad8b9c2ab0b4e4789; v=0; _tb_token_=83eb73633369; tb_city=110100; tb_cityName="sbG+qQ=="; uc1=cookie14=Uoe3d0jBPoLUJg%3D%3D; tfstk=cgxRBRf-gjclhoBvQU3mO5aNtxkGacwRt81LvY2uMTrTBqZLAsmyjhnUb46UwiHA.; l=eBxXWGBIgxwuYW4ABOfZnurza77t-IRxjuPzaNbMiOCP_yCH5wdPW63SGLTMCnMVhsiJR3-W5FX7BeYBqC2sjqj4axom4kkmn; isg=BHBwrYAd5UYS1blScd67X3qLQT7CuVQD7oFwhWrBdEueJRDPEsngk4YbfT1Fhgzb',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112ai9VBwd&city=110100',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# 切割获得json数据
content=content.split('(')[1].split(')')[0]
# print(content)
with open('040_jsonpath_taopiaopiao.json','w',encoding='utf-8') as fp:
    fp.write(content)
obj=json.load(open('040_jsonpath_taopiaopiao.json','r',encoding='utf-8'))
city_list=jsonpath.jsonpath(obj,'$..regionName')
print(city_list)