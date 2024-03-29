# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MangaItem(scrapy.Item):
    title = scrapy.Field()
    latest_chapter = scrapy.Field()
    latest_chapter_link = scrapy.Field()
    pass
