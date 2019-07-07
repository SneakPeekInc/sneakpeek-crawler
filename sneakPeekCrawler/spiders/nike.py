# -*- coding: utf-8 -*-z
import os
import scrapy
from sneakPeekCrawler.items import Sneaker

class NikeSpider(scrapy.Spider):
    name = 'nike'
    allowed_domains = ['nike.com']
    start_urls = ['https://store.nike.com/jp/ja_jp/pw/メンズ-ライフスタイル-シューズ/7puZoneZoi3?ipp=120']

    def parse(self, response):

        os.environ['ENV'] = 'dev'
        if os.environ['ENV'] == 'dev':
            counter = 0

        next_urls = response.css('div.grid-item-image')

        for next_url in next_urls:
            url = next_url.css('a::attr(href)').extract_first()
            yield scrapy.Request(url,self.parse_items)

            if os.environ['ENV'] == 'dev':
                counter += 1

                if counter == 5:
                    return

    def parse_items(self, response):

        NAME_XPATH = '//h1[@id="pdp_product_title"]/text()'
        PRICE_XPATH = '//div[@class="css-i260wg"]/text()'
        IMAGE_URLS_XPATH = "//img[contains(@src, 'https://c.static-nike.com/a/images/t_PDP_1280')]/@src"

        def string_price_format_number(price):

            price = price.translate(str.maketrans(
                {' ': None, '￥': None, ',': None}))
            price = int(price)

            return price

        item = Sneaker()
        item['name'] = response.xpath(NAME_XPATH).extract_first()
        item['price'] = string_price_format_number(response.xpath(PRICE_XPATH).extract_first())
        item['image_urls'] = response.xpath(IMAGE_URLS_XPATH).extract()

        yield item

