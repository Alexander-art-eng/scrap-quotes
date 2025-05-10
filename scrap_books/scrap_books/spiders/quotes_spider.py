import scrapy
from ..items import ScrapBooksItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = ScrapBooksItem()

        all_quotes = response.xpath(".//div[@class='quote']")
        for quote in all_quotes:
            title = quote.xpath(".//span[@class='text']//text()").extract()
            author = quote.xpath(".//small[@class='author']//text()").extract()
            tags = quote.xpath(".//a[@class='tag']//text()").extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items