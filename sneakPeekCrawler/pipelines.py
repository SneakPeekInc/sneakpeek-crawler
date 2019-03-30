# -*- coding: utf-8 -*-

import scrapy
import os
from google.cloud import storage

from PIL import Image
import numpy as np

import urllib.parse

class Pipeline(object):
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider):

        #クラウドストレージ（バケット）に接続
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./keyfile.json'
        client = storage.Client()
        bucket = client.get_bucket('sneakers')

        #バイナリデータの一時保存先
        dst_path = './datastore.jpg'

        image_url= urllib.parse.quote(item['image_urls'][0], safe='/:')

        try:
            data = urllib.request.urlopen(image_url).read()
            with open(dst_path, mode="wb") as f:
                #バイナリデータの書き込み
                f.write(data)

                blob = bucket.blob('nike/' + item['name'])
                blob.upload_from_filename(filename='./datastore.jpg')
                print(blob.public_url)

                #バイナリデータの削除
                os.remove(dst_path)

        except urllib.error.URLError as e:
            print(e)

        return item
