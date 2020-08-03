# -*- coding: utf-8 -*-
import scrapy
from mztu.items import MztuItem
from scrapy.loader import ItemLoader


class MezituSpider(scrapy.Spider):
    name = 'mezitu'
    allowed_domains = ['www.mzitu.com']

    def start_requests(self):
        start_urls = 'https://www.mzitu.com'
        yield scrapy.Request(url=start_urls, callback=self.parse, dont_filter=True)

    def parse(self, response):
        number = response.xpath('//div[@class="nav-links"]/a//text()').getall()[-2]
        urls = [f'https://www.mzitu.com/page/{i}/' for i in range(1, int(number) + 1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        datalist = response.xpath('//div[@class="postlist"]/ul/li')
        for data in datalist:
            title = data.xpath('./span/a//text()').getall()
            url = response.urljoin(data.xpath('./span/a/@href').get())
            yield scrapy.Request(url=url, callback=self.parse_images, meta={'title': title})

    def parse_images(self, response):
        number = response.xpath('//div[@class="pagenavi"]/a//text()').getall()[-2]
        urls = [f'{response.url}/{i}' for i in range(1, int(number) + 1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True,
                                 meta={'title': response.meta.get('title')})

    def parse_item(self, response):
        item = ItemLoader(item=MztuItem(), response=response)
        item.add_value('title', response.meta.get('title'))
        item.add_xpath('file_name', '//div[@class="content"]/h2[@class="main-title"]/text()')
        item.add_xpath('file_urls', '//div[@class="content"]/div/p/a/img/@src')
        yield item.load_item()
