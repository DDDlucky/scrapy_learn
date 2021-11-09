import scrapy


class QiitaTrend1dSpider(scrapy.Spider):
    name = 'qiita_trend_1d'
    allowed_domains = ['qiita.com']
    start_urls = ['https://qiita.com/']

    def parse(self, response):
        pass
