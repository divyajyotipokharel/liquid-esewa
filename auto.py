import time
import scrapy
from scrapy.crawler import CrawlerProcess
from liquid.spiders.liquid_spider import liquidSpider


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(liquidSpider)
process.start() # the script will block here until the crawling is finished

time.sleep(10)
import compare
time.sleep(5)
compare.compare_script()

time.sleep(10)
import sendemail
time.sleep(5)
sendemail.send_email()                         
