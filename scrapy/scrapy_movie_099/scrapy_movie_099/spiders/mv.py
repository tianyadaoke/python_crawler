import scrapy
from scrapy_movie_099.items import ScrapyMovie099Item

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            # 获取链接和name
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # 第二页的地址是
            url = 'https://www.ygdy8.net' + href

            print(name, url)
            #对第二页的链接进行访问
            yield scrapy.Request(url=url, callback=self.parse_second,meta={'name':name})

    def parse_second(self, response):
        # 如果拿不到数据，那就检查语法
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接收到请求的meta参数
        name=response.meta['name']
        movie=ScrapyMovie099Item(src=src,name=name)
        yield movie

