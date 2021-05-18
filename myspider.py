# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os
from datetime import datetime
from trustpilot_scraper import scrapeTrustPilot
import time 

class MySpider(CrawlSpider):
    name = 'gspider'
    allowed_domains = ['trustpilot.com']
    start_urls = [r'https://it.trustpilot.com']
    rules = (# Extract and follow all links!
        Rule(LinkExtractor(), callback='parse_item', follow=True), )
               
    def parse_item(self, response):
        if "review" in response.url:
            filename = f'{datetime.now().strftime("%Y%m%d%H%M%S%f")}.csv'
            time.sleep(1)
            myRev = scrapeTrustPilot(response.body)
            if len(myRev)>0:
                myRev.to_csv(os.path.join("data", filename))
        self.log('crawling'.format(response.url))
