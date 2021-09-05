# coding: utf-8
# @Time: 2021/9/5 17:34
# @Author: Bing
# @File: 038_xpath_download_image
# @Project: basic
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_3.html
import urllib.request
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 '
}


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content


def download(content):
    tree=etree.HTML(content)
    name_list=tree.xpath('//div[@id="container"]//a/img/@alt')
    src_list=tree.xpath('//div[@id="container"]//a/img/@src2')
    print(len(name_list),len(src_list))
    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url='https:'+src
        print(url)
        urllib.request.urlretrieve(url=url,filename='./loveimage/'+name+'.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        request=create_request(page)
        content=get_content(request)
        download(content)