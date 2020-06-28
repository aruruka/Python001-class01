# -*- coding: utf-8 -*-
import scrapy
from CrawlerMaoyan.items import CrawlermaoyanItem
from scrapy.selector import Selector


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        """
        The movie dl's selector is:
        Selector(response=response).xpath(
            '//dl[@class="movie-list"]')

        So, the movie dds' selectors are:
        Selector(response=response).xpath('//dl[@class="movie-list"]').xpath('//dd')

        You can debug if the selectors find right as below:
        self.logger.info(len(Selector(response=response).xpath(
            '//dl[@class="movie-list"]').xpath('//dd')))
        """
        movie_selector_generator = (movie for movie in Selector(
            response=response).xpath('//dl[@class="movie-list"]').xpath('//dd'))
        for i in range(10):
            item = CrawlermaoyanItem()
            movie_dd = next(movie_selector_generator)
            # self.logger.info(movie_dd.xpath('./div[2]/a/text()').extract())
            item['title'] = movie_dd.xpath('./div[2]/a/text()').extract()
            # self.logger.info(movie_dd.xpath('./div[1]/div[2]/a/div/div[2]/text()').extract()[-1].strip())
            item['genre'] = movie_dd.xpath(
                './div[1]/div[2]/a/div/div[2]/text()').extract()[-1].strip()
            # self.logger.info(movie_dd.xpath('./div[1]/div[2]/a/div/div[4]/text()').extract()[-1].strip())
            item['release_date'] = movie_dd.xpath(
                './div[1]/div[2]/a/div/div[4]/text()').extract()[-1].strip()
            yield item
