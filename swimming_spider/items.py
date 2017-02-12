# -*- coding: utf-8 -*-
import scrapy


class SwimmersItem(scrapy.Item):
    # define the fields for your item here like:
    count = scrapy.Field()
    pool_name = scrapy.Field()
    city = scrapy.Field()
