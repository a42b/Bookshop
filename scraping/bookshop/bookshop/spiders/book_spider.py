from pathlib import Path
import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "https://books.toscrape.com/catalogue/category/books_1/page-1.html",
    ]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title" : book.css("h3 a::attr(title)").get(),
                "price" : book.css("p.price_color::text").get(),
                "rating": book.css("p.star-rating::attr(class)").get().split()[-1],
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        