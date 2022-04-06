import scrapy


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['http://magnatiles.com/products/page/1']

    def parse(self, response):
        products = response.css('ul.products li')

        pass
