import scrapy
from scrapy_dangdan_094.items import ScrapyDangdan094Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果多页下载必须调整allowed_domains范围
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # src=//ul[@id="component_59"]/li/img/@src
        # alt=//ul[@id="component_59"]/li/img/@alt
        # price=//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 所有的select对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdan094Item(src=src, name=name, price=price)
            # 获取一个book就将book交给pipelines
            yield book
        # 每一页的爬取逻辑都一样，所以我们只需要执行那个页面的请求再次调用parse方法
        # http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        # http://category.dangdang.com/pg4-cp01.01.02.00.00.00.html
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            # 怎么去调用parse方法
            # 就是get请求
            yield scrapy.Request(url=url, callback=self.parse)
