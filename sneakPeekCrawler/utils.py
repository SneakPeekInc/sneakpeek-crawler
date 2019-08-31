import os

def is_development():
    return os.environ['ENV'] == 'development'

def get_brands():
    return ['nike', 'newbalance']

def crawling(brand):
    os.system("scrapy crawl " + brand)
    return "done"
