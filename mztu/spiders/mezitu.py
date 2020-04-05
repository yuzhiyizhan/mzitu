# -*- coding: utf-8 -*-
import re
import scrapy
from mztu.items import MZtujpgItem

start_urls = []
for i in range(1, 244):
    urls = f'https://www.mzitu.com/page/{i}/'
    start_urls.append(urls)


class MezituSpider(scrapy.Spider):
    name = 'mezitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = start_urls

    # start_urls = ['https://www.mzitu.com/page/243', 'https://www.mzitu.com/page/242', ]

    # def start_requests(self):
    #     start_urls = []
    #     for i in range(1, 244):
    #         urls = f'https://www.mzitu.com/page/{i}/'
    #         start_urls.append(urls)
    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        next_list = response.xpath('//div[@class="postlist"]/ul/li/a/@href').getall()
        for url in next_list:
            yield scrapy.Request(url=url, callback=self.parse_next, dont_filter=True)
        # urls = response.xpath('//div[@class="nav-links"]/a/@href').get()
        # print(urls)
        # if urls:
        #     yield scrapy.Request(url=urls, callback=self.parse, dont_filter=True)

    def parse_next(self, response):
        title = response.xpath('//div[@class="content"]/h2[@class="main-title"]/text()').get()
        try:
            category = re.findall('(.*)（.*', title)[0]
        except:
            category = title
        image = response.xpath('//div[@class="main-image"]/p/a/img/@src').get()
        next_str = response.xpath('//div[@class="pagenavi"]/a/span/text()').getall()[-1]
        file_urls = image
        item = MZtujpgItem(category=category, file_urls=[file_urls])
        yield item
        if '下一页' in next_str:
            url = response.xpath('//div[@class="pagenavi"]/a/@href').getall()[-1]
            yield scrapy.Request(url=url, callback=self.parse_next, dont_filter=True)
