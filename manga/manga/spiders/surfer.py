from pathlib import Path
from typing import Iterable, Any
from ..items import MangaItem

import scrapy
from scrapy import Request
from scrapy.http import Response


class MangaSpider(scrapy.Spider):
    name = "mangacrawler"
    start_urls = ['https://mangaclash.com/manga/maou-ni-natta-node-dungeon-tsukutte-jingai-musume-to-honobono-suru/']

    def parse(self, response):
        title = response.css('.post-title h1::text').get()
        latest_chapter = response.css('.wp-manga-chapter a::text').get()
        latest_chapter_link = response.css('.wp-manga-chapter a::attr(href)').get()

        manga_item = MangaItem(title=title, latest_chapter=latest_chapter, latest_chapter_link=latest_chapter_link)
        yield manga_item

        self.log(f"Title: {title}, Latest Chapter: {latest_chapter}, Latest Chapter Link: {latest_chapter_link}")





