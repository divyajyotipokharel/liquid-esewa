import scrapy
from scrapy import Spider
import csv
from liquid.items import LiquidItem, Field
from scrapy.selector import HtmlXPathSelector

class liquidSpider(Spider):
    name = "liquid"
    allowed_domains = ["esewapasal.com"]
    
    def start_requests(self):
        urls = [
            'https://www.esewapasal.com/liquor-tobacco.html'
        ]
        for url in urls:
            print("Scrapping here")
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("processing:"+response.url)
        hxs = HtmlXPathSelector(response)
        title = hxs.select("//h2[@class='product name product-name product-item-name']/a/text()").getall()
        price = hxs.select('//span[@data-price-type="finalPrice"]/span/text()').getall()
        print("done")
        print(title)
        print(price)
        print("done here")
        with open('new_result.csv', 'a') as csvfile:
            for i in range(len(title)):
                csvfile.write(title[i])
                csvfile.write('*')
                csvfile.write(price[i])
                csvfile.write('\n')
        print("writing to file")
        next_page = response.css('li.item.pages-item-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

