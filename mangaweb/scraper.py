from manga.manga.spiders.surfer import MangaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals

def scrape_manga(manga_title):
    process = CrawlerProcess()

    # Create a list to store scraped items
    scraped_items = []

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
        print(f"IF this has anything: {scraped_items}")
        return scraped_items
    else:
        # Return default values
        default_item = {
            'title': 'Default Title',
            'latest_chapter': 'Default Latest Chapter',
            'latest_chapter_link': 'Default Latest Chapter Link'
        }
        return default_item
