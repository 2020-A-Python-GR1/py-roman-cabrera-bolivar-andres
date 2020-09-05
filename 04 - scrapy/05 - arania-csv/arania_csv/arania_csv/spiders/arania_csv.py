from scrapy.spiders import CSVFeedSpider

class VinosBlancosArania(CSVFeedSpider):

    name = "vinos"

    start_urls = [
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    ]
    delimiter = ';'
    quitechar = '"'
    headers = [
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'quality'
        ]
    
    def parse_row(self, response, row):
        print(type(row))
        with open('vinos.txt', 'a+', encoding='utf-') as archivo:
            archivo.write('Densidad:' + row['fixed density'] + 'Alcohol' + row['alcohol'] + '\n')