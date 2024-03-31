from pathlib import Path
from typing import Iterable, Any
from ..items import MangaItem

import scrapy
from scrapy import Request
from scrapy.http import Response

class MangaSpider(scrapy.Spider):
    name = "mangacrawler"

    def __init__(self, manga_title=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        manga_title = manga_title.replace(":", "")
        manga_title = manga_title.replace(" ", "-")
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



