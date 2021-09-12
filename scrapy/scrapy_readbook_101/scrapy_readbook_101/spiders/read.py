import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_101.items import ScrapyReadbook101Item
# 创建项目 scrapy startproject readbook
# 跳转到spider目录下 scrapy genspider -t crawl 爬虫文件名字 爬取域名
class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1090_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1090_\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        img_list=response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name=img.xpath('./data-original').extract_first()
            src=img.xpath('./@alt').extract_first()
            book=ScrapyReadbook101Item(name=name,src=src)
        yield book
