import scrapy

site_idx = 0

def humanize(data):
	humanized_data = data[2:-2]
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
		data = data.encode()
		filename = '%d.txt' % site_idx
		site_idx += 1
		with open(filename, 'wb') as f:
			f.write(data)
