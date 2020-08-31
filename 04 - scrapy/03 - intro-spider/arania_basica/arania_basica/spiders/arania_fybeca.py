import scrapy

class IntroSpider(scrapy.Spider):
    name = 'fybeca'
    urls = ['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        container_tag = response.css('article.product_pod')