import os
import sys
from sneakPeekCrawler import utils
from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    os.chdir("sneakPeekCrawler")
    for brand in utils.brandsInfo():
        os.system("scrapy crawl " + brand)
    os.chdir("..")
    return "ok"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

