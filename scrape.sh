#!/bin/bash

cd URL_spider/url
python3 -m scrapy crawl url_spider
mv toscrape.txt ../../BB_spider/bb/
cd ../../BB_spider/bb
python3 -m scrapy crawl bb_spider
