# coding: utf-8
# @Time: 2021/9/3 14:10
# @Author: Bing
# @File: 021_urlib_download
# @Project: basic
import  urllib.request
# 也可以下载视频和图片
url_page="http://www.baidu.com"
urllib.request.urlretrieve(url_page,'baidu.html')
