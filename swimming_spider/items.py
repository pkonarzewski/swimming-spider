# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SwimmersItem(scrapy.Item):
    # define the fields for your item here like:
    count = scrapy.Field()
    pool_name = scrapy.Field()
    city = scrapy.Field()
