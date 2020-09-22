import scrapy
import pandas as pd

class MovieCrawl(scrapy.Spider):
    name = 'movie_spyder'


    def start_requests(self):
        urls = [
        'https://www.mirandopeliculas.com/page/1',
        'https://www.mirandopeliculas.com/page/2',
        'https://www.mirandopeliculas.com/page/3',
        'https://www.mirandopeliculas.com/page/4',
        'https://www.mirandopeliculas.com/page/5',
        'https://www.mirandopeliculas.com/page/6',
        'https://www.mirandopeliculas.com/page/7',
        'https://www.mirandopeliculas.com/page/8',
        'https://www.mirandopeliculas.com/page/9',
        'https://www.mirandopeliculas.com/page/10'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse (self, response):
        container = response.css('div.pelicula')
        names = list(container.css('h2::text').extract())
        desc_raw = list(container.css('div.sinopsis::text').extract())

        
        

