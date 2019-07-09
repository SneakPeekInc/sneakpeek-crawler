# -*- coding: utf-8 -*-
import os
import scrapy
from sneakPeekCrawler.items import Sneaker

class NewBalanceSpider(scrapy.Spider):
    name = 'newbalance'
    allowed_domains = ['newbalance.jp']
    start_urls = ['https://shop.newbalance.jp/shop/goods/search.aspx?filtercode5=M&filtercode6=100&min_price=&max_price=&tree1=&keyword=']

    def parse(self, response):

        next_urls = response.css('div.StyleP_Item_.item')

        for n, next_url in enumerate(next_urls):
            url = next_url.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(url), self.parse_items)

            if os.environ['ENV'] == 'dev' and n > 3: return

    def parse_items(self, response):

        NAME_XPATH = '//div[@class="main"]/h3/text()'
        PRICE_XPATH = '//div[@class="main"]/p[@class="price"]/span/text()'
        IMAGE_URLS_XPATH = "//a[@class='active']/img/@src"

        def string_price_format_number(price):
            price = price.translate(str.maketrans(
                {',': None, '円': None, '＋': None, '(': None, '税': None, ')': None}))
            price = int(price)

            return price

        def image_url_format(url):
            url = response.urljoin(url)
            url = url.replace('L_T', 'L_O')

            return url

        item = Sneaker()
        item['name'] = response.xpath(NAME_XPATH).extract_first()
        item['price'] = string_price_format_number(
            response.xpath(PRICE_XPATH).extract_first())
        item['image_urls'] = image_url_format(
            response.xpath(IMAGE_URLS_XPATH).extract_first())

        yield item
