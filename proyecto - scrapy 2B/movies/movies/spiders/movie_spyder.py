import scrapy
import pandas as pd
import numpy as np
import re

class MovieCrawl(scrapy.Spider):
    name = 'movie_spyder'
    urls = []
    size_page = np.arange(1,1000,50)

    for num in size_page:
        urls.append('https://www.imdb.com/search/title/?groups=top_1000&start={num}'.format(num=num))


    m_name = []
    m_year = []
    m_rated = []
    m_duration = []
    m_genre = []
    m_rating = []
    m_metascore = []
    m_director = []
    m_votes = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        movies_list = response.css('div.lister-item')
        for movie in movies_list:
            name = movie.css('h3 > a::text').extract_first()
            year = movie.css('h3 > span.lister-item-year::text').extract_first()
            rated = movie.css('p.text-muted > span.certificate::text').extract_first()
            duration = movie.css('p.text-muted > span.runtime::text').extract_first()
            genre = movie.css('p.text-muted > span.genre::text').extract_first()
            rating = movie.css('div.ratings-bar > div.inline-block::attr(data-value)').extract_first()
            metascore = movie.css('div.ratings-bar > div.inline-block > span.metascore::text').extract_first()
            director = movie.css('p > a::text').extract_first()
            votes = movie.css('p.sort-num_votes-visible > span::attr(data-value)').extract_first()
            self.m_name.append(name)
            self.m_year.append(re.sub('[(\D)]', '', str(year)))
            self.m_rated.append(rated)
            self.m_genre.append(str(genre).split(',')[0].strip('\n').strip())
            self.m_duration.append(str(duration).strip('min '))
            self.m_rating.append(rating)
            if str(metascore).strip() == 'None':
                self.m_metascore.append(0)
            else:
                self.m_metascore.append(int(str(metascore).strip()))

            self.m_director.append(director)
            self.m_votes.append(votes)
            

    def close(self, reason):
        df = pd.DataFrame({
            'name' : pd.Series(self.m_name),
            'year' : pd.Series(self.m_year),
            'rated' : pd.Series(self.m_rated),
            'duration_min' : pd.Series(self.m_duration),
            'genre' : pd.Series(self.m_genre),
            'rating' : pd.Series(self.m_rating),
            'metascore' : pd.Series(self.m_metascore),
            'director' : pd.Series(self.m_director),
            'votes' : pd.Series(self.m_votes)
        })
        df.to_csv('data.csv', index = False, encoding='utf-8')