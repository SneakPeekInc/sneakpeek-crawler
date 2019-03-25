# -*- coding: utf-8 -*-
import scrapy
from sneakPeekCrawler.items import Sneaker


class NikeSpider(scrapy.Spider):
    name = 'nike'
    allowed_domains = ['store.nike.com/jp/ja_jp/pw']
    start_urls = ['https://store.nike.com/jp/ja_jp/pw//']

    def parse(self, response):
        image_doms = response.css('div.exp-gridwall-content.clearfix')
        for image_dom in image_doms:
            item = Sneaker()
            item['url'] = image_dom.css('img::attr(src)').extract()
            yield item
