import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://m.58.com/hz/sou/?key=%E5%89%8D%E7%AB%AF']
    start_urls = ['https://m.58.com/hz/sou/?key=%E5%89%8D%E7%AB%AF/']

    def parse(self, response):
        #字符串
        # content=response.text
        # #二进制
        # content=response.body
        print('======================================')
        # print(content)

        #可以直接使用xpath语法
        response.xpath('')

