import scrapy

class IntroSpider(scrapy.Spider):
    name = 'intro_spider'
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        container_tag = response.css('article.product_pod')
        titles = container_tag.css('h3 > a::text').extract()
        prices = container_tag.css('div.product_price > p.price_color::text').extract()
        stocks = container_tag.css('div.product_price > p.instock::text').extract()
        images = container_tag.css('div.image_container img::attr(src)').extract()
        print(titles)
        print(prices)
        print(stocks)
        print(images)
    
    