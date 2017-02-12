# -*- coding: utf-8 -*-
import scrapy


class AquariumSpider(scrapy.Spider):
    name = "aquarium"
    allowed_domains = ["http://www.basen-ostroleka.pl"]
    start_urls = ['http://http://www.basen-ostroleka.pl/']

    def parse(self, response):
        pass
