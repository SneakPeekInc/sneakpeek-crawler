import os

def is_development():
    return os.environ['ENV'] == 'development'

def get_brands():
    return ['nike', 'newbalance']

def crawling(brand):
    os.chdir("sneakPeekCrawler")
    os.system("scrapy crawl " + brand)
    os.chdir("..")
    return "done"

