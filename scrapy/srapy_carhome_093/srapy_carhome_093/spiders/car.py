import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn/price/brand-15.html']
    start_urls = ['http://car.autohome.com.cn/price/brand-15.html']  # 后缀html不允许加/

    def parse(self, response):
        print('==============================')
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)
