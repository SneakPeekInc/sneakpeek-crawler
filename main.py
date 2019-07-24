import os
import sys
from sneakPeekCrawler import utils
from flask import Flask
app = Flask(__name__)


@app.route('/nike', methods=['GET'])
def nikeCrawl():
    os.chdir("sneakPeekCrawler")
    os.system("scrapy crawl nike")
    os.chdir("..")
    return "done"


@app.route('/newbalance', methods=['GET'])
def newbalanceCrawl():
    os.chdir("sneakPeekCrawler")
    os.system("scrapy crawl newbalance")
    os.chdir("..")
    return "done"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

