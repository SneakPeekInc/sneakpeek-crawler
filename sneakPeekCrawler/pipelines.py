# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from . import utils
from google.cloud import firestore

class SneakpeekcrawlerPipeline(object):

    def __init__(self, collection_name):
        self.collection_name = 'sneakers'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            collection_name=crawler.spider.name
        )

    def open_spider(self, spider):
        self.client = firestore.Client.from_service_account_json(
           os.environ['SERVICE_ACCOUNT'] )
        self.db = self.client.collection(self.collection_name)

    def process_item(self, item, spider):
        result = self.db.add(dict(item))
        if utils.isDevelopment():
            self.db.document(result[1].id).delete()
        return item
