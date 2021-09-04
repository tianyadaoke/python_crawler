# coding: utf-8
# @Time: 2021/9/4 16:51
# @Author: Bing
# @File: 029_ajax_post_kfc
# @Project: basic
# url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# cname: 杭州
# pid:
# pageIndex: 1
# pageSize: 10
import urllib.request
import urllib.parse

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}


def create_request(page):
    data = {
        'cname': '杭州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def download(content, page):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(content,page)
