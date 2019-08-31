import os
import sys
from sneakPeekCrawler import utils
from flask import Flask
app = Flask(__name__)


@app.route('/nike', methods=['GET'])
def nike_crawl():
    return utils.crawling("nike")


@app.route('/newbalance', methods=['GET'])
def newbalance_crawl():
    return utils.crawling("newbalance")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

