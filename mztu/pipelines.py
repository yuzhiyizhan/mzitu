# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.files import FilesPipeline


class MztuPipeline(object):
    def process_item(self, item, spider):
        return item


# class MZTImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         requests_objs = super(MZTImagesPipeline, self).get_media_requests(item, info)
#         for requests_obj in requests_objs:
#             requests_obj.item = item
#         return requests_objs
#
#     def file_path(self, request, response=None, info=None):
#         path = super(MZTImagesPipeline, self).file_path(request, response, info)
#         category = request.item.get('category')
#         images_store = IMAGES_STORE
#         category_path = os.path.join(images_store, category)
#         if not os.path.exists(category_path):
#             os.mkdir(category_path)
#         image_name = path.replace('full/', '')
#         image_path = os.path.join(category_path, image_name)
#         return image_path


class MZFilesPipline(FilesPipeline):
    def get_media_requests(self, item, info):
        requests_objs = super(MZFilesPipline, self).get_media_requests(item, info)
        for requests_obj in requests_objs:
            requests_obj.item = item
        return requests_objs

    def file_path(self, request, response=None, info=None):
        path = super(MZFilesPipline, self).file_path(request, response, info)
        category = request.item.get('category')
        image_name = path.replace('full/', '')
        image_path = os.path.join(category, image_name)
        return image_path
