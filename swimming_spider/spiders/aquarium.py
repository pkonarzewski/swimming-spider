# -*- coding: utf-8 -*-
import scrapy
from swimming_spider.items import SwimmersItem


class AquariumSpider(scrapy.Spider):
    name = "aquarium"
    start_urls = ['http://www.basen-ostroleka.pl/']

    # Items default variables
    pool_name = "Aquarium"
    city = "Ostrołęka"

    def parse(self, response):
        users = response.xpath('//div[@class="left"]/div/h3[text() = "Osób na basenie"]/following-sibling::div/text()').extract_first().strip()
        yield SwimmersItem(
            ppl_nr=int(users),
            pool_name=self.pool_name,
            city=self.city
        )
