from manga.manga.spiders.surfer import MangaSpider
from scrapy.crawler import CrawlerProcess

def scrape_manga(manga_title):
    process = CrawlerProcess()
    process.crawl(MangaSpider, manga_title=manga_title)
    process.start()
