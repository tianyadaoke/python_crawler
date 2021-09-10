# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道就必须再settings中开启管道
class ScrapyDangdan094Pipeline:
    # 在爬虫文件开始之前执行
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        # 'w‘必须要写str，不能是对象
        # 'w'会每个对象都打开一次文件，覆盖之前的内容
        # 以下模式不推荐，打开文件过于频繁
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item


# 多条管道同时开启
# 定义管道类
# 在settings中开启管道
import urllib.request
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url='http:'+item.get('src')
        filename='./books/'+item.get('name')+'.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)
        return item
