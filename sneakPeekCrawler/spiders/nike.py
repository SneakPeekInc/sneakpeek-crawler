# -*- coding: utf-8 -*-
import scrapy
from sneakPeekCrawler.items import Sneaker


class NikeSpider(scrapy.Spider):
    name = 'nike'
    allowed_domains = ['nike.com']
    start_urls = ['https://store.nike.com/jp/ja_jp/pw/メンズ-ライフスタイル-シューズ/7puZoneZoi3?ipp=120']


    def parse(self, response):
        # テスト用コード
        returnCounter = 0
        next_urls = response.css('div.grid-item-image')
        for next_url in next_urls:
            url = next_url.css('a::attr(href)').extract_first()
            yield scrapy.Request(url,self.parse_items)

            # テスト用コード ループ5回でreturn
            returnCounter += 1
            if returnCounter >= 5:
                return


    def parse_items(self, response):
        item = Sneaker()
        item['name'] = response.css('h1#pdp_product_title.fs26-sm.fs28-lg.css-33lwh4').extract_first()
        item['price'] = response.css('div.mb-1-sm.text-color-black').extract_first()
        item['image_urls'] = response.css('img.css-viwop1.u-full-width.u-full-height.css-m5dkrx::attr(src)').extract()
        yield item
