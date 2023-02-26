# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaochinhphuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title=scrapy.Field()
    news_href=scrapy.Field()
    news_date=scrapy.Field()

class yuenanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title=scrapy.Field()
    news_href=scrapy.Field()
    news_date=scrapy.Field()

class yinduspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title=scrapy.Field()
    news_href=scrapy.Field()
    news_date=scrapy.Field()

class pakistanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title=scrapy.Field()
    news_href=scrapy.Field()
    news_date=scrapy.Field()

