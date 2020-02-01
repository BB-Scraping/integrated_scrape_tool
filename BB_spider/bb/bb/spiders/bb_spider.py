import scrapy
import re
import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

site_idx = 0

def humanize(data):
	humanized_data = data[2:-2]
	humanized_data = humanized_data.replace("\\r", " ")
	humanized_data = humanized_data.replace("\\n", " ")
	humanized_data = humanized_data.replace("\', \'", "")
	humanized_data = humanized_data.replace("\',", "")
	humanized_data = humanized_data.replace(", \'", "")
	humanized_data = humanized_data.replace("\\xa0", "")
	return humanized_data

class bb_spider(scrapy.Spider):
	name = 'bb_spider'
	f = open('toscrape.txt', 'r')
	start_urls = f.read().splitlines()
	def parse(self, response):
		global site_idx
		page = response.url.split('/')[-1]
		data = str(response.css('#ctl00_MainContentPlaceholder_C006_forumsFrontendPostsList_ctl00_ctl00_list_ctrl0_ContentHtml *::text').getall())
		data = humanize(data)
		site_idx += 1
		sheet1.write(site_idx, 0, data)
		wb.save('output.xls')