# -*- coding: utf-8 -*-
import scrapy
from sneakPeekCrawler.items import SneakpeekcrawlerItem



class NikeSpider(scrapy.Spider):
    name = 'nike'
    allowed_domains = ['store.nike.com/jp/ja_jp/pw']
    start_urls = ['https://store.nike.com/jp/ja_jp/pw//']

    def parse(self, response):
        for nike in response.css('div.exp-gridwall-content.clearfix'):
            item = SneakpeekcrawlerItem()
            item['url'] = nike.css('img::attr(src)').extract()
            yield item
