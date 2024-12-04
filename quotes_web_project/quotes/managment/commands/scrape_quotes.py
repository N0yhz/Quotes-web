# management/commands/scrape_quotes.py
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_scraper.quotes_scraper.spiders.quote_spider import QuotesSpider

class Command(BaseCommand):
    help = 'Run the quotes Scrapy spider'

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(QuotesSpider)
        process.start()
