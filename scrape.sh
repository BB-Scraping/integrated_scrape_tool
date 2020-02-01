#!/bin/bash

for((i=2;i<23;i++))
do
	echo https://www.beyondblue.org.au/get-support/online-forums/depression/page/"$i" >> raw.txt
done
mv raw.txt URL_spider/url
cd URL_spider/url
python3 -m scrapy crawl url_spider
mv toscrape.txt ../../BB_spider/bb/
cd ../../BB_spider/bb
python3 -m scrapy crawl bb_spider
mv output.xls ../../
