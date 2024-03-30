from pathlib import Path
from typing import Iterable, Any
from ..items import MangaItem

import scrapy
from scrapy import Request
from scrapy.http import Response


# class MangaSpider(scrapy.Spider):
#     name = "mangacrawler"
#     start_urls = ['https://mangaclash.com/manga/maou-ni-natta-node-dungeon-tsukutte-jingai-musume-to-honobono-suru/']
#
#     def parse(self, response):
#         title = response.css('.post-title h1::text').get()
#         latest_chapter = response.css('.wp-manga-chapter a::text').get()
#         latest_chapter_link = response.css('.wp-manga-chapter a::attr(href)').get()
#
#         item = MangaItem()
#         item['title'] = title
#         item['latest_chapter'] = latest_chapter
#         item['latest_chapter_link'] = latest_chapter_link
#
#         yield item
#         # yield {
#         #     'title': title, 'latest_chapter' : latest_chapter, 'link' : latest_chapter_link
#         # }
#
#         #self.log(f"This is it man: {item}")


class MangaSpider(scrapy.Spider):
    name = "mangacrawler"

    def __init__(self, manga_title=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://mangaclash.com/manga/{manga_title}/']

    def parse(self, response):
        title = response.css('.post-title h1::text').get()
        latest_chapter = response.css('.wp-manga-chapter a::text').get()
        latest_chapter_link = response.css('.wp-manga-chapter a::attr(href)').get()

        item = {
            'title': title,
            'latest_chapter': latest_chapter,
            'latest_chapter_link': latest_chapter_link
        }

        yield item



