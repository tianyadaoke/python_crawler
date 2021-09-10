# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdan094Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗的说就是你要下载的数据有什么
    # 图书
    src = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 分类
    price = scrapy.Field()
