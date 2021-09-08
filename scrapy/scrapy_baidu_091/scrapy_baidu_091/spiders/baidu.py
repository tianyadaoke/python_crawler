import scrapy


class BaiduSpider(scrapy.Spider):
    #爬虫的名字
    name = 'baidu'
    #允许访问的域名
    allowed_domains = ['www.baidu.com']
    #第一次要访问的域名
    start_urls = ['http://www.baidu.com/']

    #执行了start_urls后返回的response
    def parse(self, response):
        print('你好')
