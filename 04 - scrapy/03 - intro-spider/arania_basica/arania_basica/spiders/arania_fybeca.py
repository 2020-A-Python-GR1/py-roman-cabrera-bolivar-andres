import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class FybecaCrawl(CrawlSpider):
    name = 'arania_fybeca'

    allowed_domains = [ # heredado
        'fybeca.com'
    ]

    sizeSearch = '4000'


    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&pp={}&s=-1'.format(sizeSearch),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&pp={}&s=-1'.format(sizeSearch),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&pp={}&s=-1'.format(sizeSearch),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&pp={}&s=-1'.format(sizeSearch),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&pp={}&s=-1'.format(sizeSearch),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&pp={}&s=-1'.format(sizeSearch),
    ]


    segment_allowed_urls = ( 
        'cat=446&pp={}&s=-1'.format(sizeSearch),
        'cat=537&pp={}&s=-1'.format(sizeSearch),
        'cat=627&pp={}&s=-1'.format(sizeSearch),
        'cat=558&pp={}&s=-1'.format(sizeSearch),
        'cat=489&pp={}&s=-1'.format(sizeSearch),
        'cat=562&pp={}&s=-1'.format(sizeSearch),
    )

    segment_restricted_urls = (
        'pages/detail.jsf'
    )

    myRule = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segment_allowed_urls,
                deny = segment_restricted_urls,
            ),
            callback= 'parse_page'
        ),
        #empty
    )


    rules = myRule

    def parse_page(self, response):
        container_tag = response.css(
            "div.product-tile-inner"
            )

        names = list(container_tag.css(
            "a.name::text"
            ).extract())

        price_raw = list(container_tag.css(
            "div.detail > div.side > div.price::attr(data-bind)"
            ).extract())

        special_price_raw = list(container_tag.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
            ).extract())

        special_price = list()
        for item in special_price_raw:
            data = float(item.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            special_price.append(data)
        
        print("Más caro afiliado: "+ str(max(special_price)))
        print("Más barato afiliado: "+ str(min(special_price)))
        print("Suma Afiliado: "+str(sum(special_price)))

        price = list()
        for item in price_raw:
            data = float(item.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            price.append(data)
        
        print("Más caro afiliado: "+ str(max(price)))
        print("Más barato afiliado: "+ str(min(price)))
        print("Suma Afiliado: "+str(sum(price)))

        sum_price = sum(price)
        sum_special_price = sum(special_price)
        print("Ahorro: " + str(sum_price - sum_special_price))

        result = pd.DataFrame(zip(names,
                                    price, 
                                    special_price), columns=['products','price', 'special_price'])
        result['saving'] = result['price'] - result['special_price']
        result.to_csv('data.csv', index=False)