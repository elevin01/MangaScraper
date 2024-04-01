from manga.manga.spiders.surfer import MangaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals
import re

def extract_chapter_number(input_string):
    pattern = r'Chapter (\d+(\.\d+)?)'
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return None

def fixlinks(input):
    pattern = r'[,":?~!.\']'
    input = re.sub(pattern, "", input)
    return input

def scrape_manga(manga_title):
    process = CrawlerProcess()

    # Create a list to store scraped items
    scraped_items = []

    # Gets rid of special characters
    manga_title = fixlinks(manga_title)

    # Define a callback function to capture scraped items
    def capture_item(item, response, spider):
        scraped_items.append(item)

    # Connect the spider_closed signal to the callback function
    dispatcher.connect(capture_item, signal=signals.item_scraped)

    # Start crawling with the specified spider
    process.crawl(MangaSpider, manga_title=manga_title)
    process.start()

    # Check if scraped_items is not empty, otherwise return default values
    if scraped_items:
        for item in scraped_items:
            chapter_number = extract_chapter_number(item['latest_chapter'])
            if chapter_number:
                item['latest_chapter'] = chapter_number
        return scraped_items
    else:
        # Return default values
        default_item = {
            'title': 'Default Title',
            'latest_chapter': 'Default Latest Chapter',
            'latest_chapter_link': 'Default Latest Chapter Link'
        }
        return default_item
