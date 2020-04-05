# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MztuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class MZtujpgItem(scrapy.Item):
    # category = scrapy.Field()
    # image_urls = scrapy.Field()
    # images = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    category = scrapy.Field()