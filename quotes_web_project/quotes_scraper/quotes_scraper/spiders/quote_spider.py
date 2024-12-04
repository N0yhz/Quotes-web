import scrapy
from quotes.models import Quote, Tag, Author

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://127.0.0.1:8000/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote = quote.css('span.text::text').get()
            author = quote.css('span.author::text').get()
            tags = quote.css('div.tags a::text').getall()

            author = Tag.objects.get_or_create(name=author)
            quote = Quote.objects.get_or_create(quote=quote, author=author)

            for tag in tags:
                tag = Tag.objects.get_or_create(tag=tag)
                quote.tags.add(tag)

            quote.save()