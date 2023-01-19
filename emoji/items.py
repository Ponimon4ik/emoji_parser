# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EmojiItem(scrapy.Item):
    name = scrapy.Field()
    image_url64 = scrapy.Field()
    image_url128 = scrapy.Field()
