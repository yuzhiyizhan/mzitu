# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import mimetypes
from scrapy.pipelines.files import FilesPipeline


class MztuPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        requests_objs = super(MztuPipeline, self).get_media_requests(item, info)
        for requests_obj in requests_objs:
            requests_obj.item = item
        return requests_objs

    def file_path(self, request, response=None, info=None):
        title = request.item.get('title')
        media_guid = request.item.get('file_name')
        media_ext = os.path.splitext(request.url)[1]
        if media_ext not in mimetypes.types_map:
            media_ext = ''
            media_type = mimetypes.guess_type(request.url)[0]
            if media_type:
                media_ext = mimetypes.guess_extension(media_type)
        return rf'{title}\{media_guid}{media_ext}'
