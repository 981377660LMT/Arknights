# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ArknightsItem(scrapy.Item):
    中文文本 = scrapy.Field()
    日文文本 = scrapy.Field()
   
