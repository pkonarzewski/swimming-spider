# -*- coding: utf-8 -*-
import scrapy
from swimming_spider.items import SwimmersItem


class AquariumSpider(scrapy.Spider):
    name = "aquarium"
    start_urls = ['http://www.basen-ostroleka.pl/']

    def parse(self, response):
        users = response.xpath('//div[@class="left"]/div/h3[text() = "Osób na basenie"]/following-sibling::div/text()').extract_first().strip()
        yield SwimmersItem(
            count=int(users),
            pool_name="Aquarium",
            city="Ostrołęka"
        )
