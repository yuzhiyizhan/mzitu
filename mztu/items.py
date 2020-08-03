# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Compose
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose


def replace_(string):
    return string.replace(' ', '')


def clean(string):
    string = string.replace('\\', '')
    string = string.replace('/', '')
    string = string.replace('|', '')
    string = string.replace(':', '')
    string = string.replace('*', '')
    string = string.replace('?', '')
    string = string.replace('"', '')
    string = string.replace('<', '')
    string = string.replace('>', '')
    return string


class MztuItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(replace_, clean),
        output_processor=TakeFirst(),
    )
    files = scrapy.Field(
        input_processor=MapCompose(replace_),
        output_processor=TakeFirst(),
    )
    file_urls = scrapy.Field(
        input_processor=MapCompose(replace_),
        output_processor=Compose(),
    )
    file_name = scrapy.Field(
        input_processor=MapCompose(replace_),
        output_processor=TakeFirst(),
    )
