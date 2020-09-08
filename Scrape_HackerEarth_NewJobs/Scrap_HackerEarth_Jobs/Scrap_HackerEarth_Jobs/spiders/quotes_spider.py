import scrapy
from ..items import ScrapHackerearthJobsItem

class QuoteSpider(scrapy.Spider):
    name = "QuotesScrapper"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        items = ScrapHackerearthJobsItem()
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tag_data = quotes.css(".tag::text").extract()

            items["title"] = title
            items["author"] = author
            items["tags"] = tag_data
            yield items