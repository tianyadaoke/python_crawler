# coding: utf-8
# @Time: 2021/9/4 13:41
# @Author: Bing
# @File: 026_post_baidutranslate
# @Project: basic
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    'Cookie': 'BIDUPSID=0921B50AAD10299102F8B40C9C432DD5; PSTM=1630671460; BAIDUID=0921B50AAD102991BDE027CB76F3502A:FG=1; BAIDUID_BFESS=0921B50AAD102991BDE027CB76F3502A:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1630702720,1630754908; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1630754908; ab_sr=1.0.1_M2ExMWQzYzNhM2U5N2NlYjJiYzJmNzNiYWI0NDk2ZGM1ZjUzZjYzM2E2ZmNlZjlkNmJhNmE4NGJmMDU5YTIxYjM3MzE5N2MzZTQ3MWM5NzU4YzJjOWFiNmZkNjQ5ZThjOTAxY2Q5YzNlZTQwNmI2OWQwOTRjNzJjMTE0NTNjZjc2ZTUwOTllODUyMWYwNjAxN2E3MWJkNDFkNTYyMGNhMQ==; __yjs_st=2_OTE3OTdlNTYwZWQ3Yzk2ZGFjNTA4M2QwNDY4YzcxYzNiMzNkNmU5NTE3ZjA1OTk2YmViZjdkN2FiZDU2YTM0MmI1OTMxODljZTlhMDcyNWIyZTMxZDM4MTAyNjgyMDliMTgyMDQzYTQ3NWY5MWIxYTYwMDIzOGU0YzdlODU4ZDViZjY5NjJiNjhkZjI5YzdjN2QxNzAxOTU0NDY2MTNkMmFlNmNiYmIxNjdhZjNiZmMzOGEzNzJjMWJlMzhlMGFkN2RhNDgyZmRhZDRjYWU0MDUyN2VmOTgxYjc4Zjc3ODc2NDg3Y2E4Y2Y1ZmVjMTYwMDgyOTc3OTcwYzZmYWExMV83XzE1OWNlZjFj'
}
data = {
    'from': 'zh',
    'to': 'en',
    'query': '草莓',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '62888.267929',
    'token': 'c2e196640e5989f03890beb355559b95',
    'domain': 'common'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)
