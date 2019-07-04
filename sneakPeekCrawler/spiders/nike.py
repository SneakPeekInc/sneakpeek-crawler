# -*- coding: utf-8 -*-
import scrapy
from sneakPeekCrawler.items import Sneaker

class NikeSpider(scrapy.Spider):
    name = 'nike'
    allowed_domains = ['nike.com']
    start_urls = ['https://store.nike.com/jp/ja_jp/pw/メンズ-ライフスタイル-シューズ/7puZoneZoi3?ipp=120']

    def parse(self, response):

        counter = 0     #テスト用

        next_urls = response.css('div.grid-item-image')

        for next_url in next_urls:
            url = next_url.css('a::attr(href)').extract_first()
            yield scrapy.Request(url,self.parse_items)

            counter += 1  # テスト用

            if counter == 5:  # テスト用
                return  # テスト用

    def parse_items(self, response):

        NAME_XPATH = '//h1[@id="pdp_product_title"]/text()'
        PRICE_XPATH = '//div[@class="css-i260wg"]/text()'
        IMAGE_URL_XPATH = '//img[@class="css-viwop1 u-full-width u-full-height css-m5dkrx"]/@src'

        def string_price_format_number(price):

            price = price.translate(str.maketrans(
                {' ': None, '￥': None, ',': None}))
            price = int(price)

            return price

        item = Sneaker()
        item['name'] = response.xpath(NAME_XPATH).extract_first()
        item['price'] = string_price_format_number(response.xpath(PRICE_XPATH).extract_first())
        item['image_urls'] = response.xpath(IMAGE_URL_XPATH).extract_first()

        yield item

