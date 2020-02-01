import scrapy

base_url = 'https://www.beyondblue.org.au/get-support/online-forums/depression'

def urlize(string):
    urlized_string = base_url + string[4:-2]    
    return urlized_string

class url_spider(scrapy.Spider):
    name = 'url_spider'
    f = open('raw.txt', 'r')
    start_urls = f.read().splitlines()
    def parse(self, response):
        global site_idx
        page = response.url.split('/')[-1]
        for i in range(0, 49):
            target = '#ctl00_MainContentPlaceholder_C006_forumsFrontendThreadsList_ctl00_ctl00_Repeater_ctrl' + str(i) + '_hlThreadTitle *::attr(href)'
            data = str(response.css(target).getall())
            data = urlize(data)
            filename = 'toscrape.txt'
            with open(filename, 'a+') as f:
                f.write(data)
                f.write('\n')
