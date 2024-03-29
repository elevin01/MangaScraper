from pathlib import Path
from typing import Iterable, Any

import scrapy
from scrapy import Request
from scrapy.http import Response


class MangaSpider (scrapy.Spider):
    name = "mangacrawler"

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)




