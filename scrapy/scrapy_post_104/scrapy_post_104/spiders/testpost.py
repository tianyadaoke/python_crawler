import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    # post必须携带参数，所以start_url没用，parse也没用
    # start_urls = ['https://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #     pass
    def start_requests(self):
        url='https://fanyi.baidu.com/sug'
        data={
            'kw':'apple'
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)
    def parse_second(self,response):
        content=response.text
        obj=json.loads(content,encoding='utf-8')
        print(obj)