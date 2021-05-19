# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os
from datetime import datetime
from trustpilot_scraper import scrapeTrustPilot
import time 

def file_folder_exists(path: str):
    """
    Return True if a file or folder exists.

    :param path: the full path to be checked
    :type path: str
    """
    try:
        os.stat(path)
        return True
    except:
        return False

def select_or_create(path: str):
    """
    Check if a folder exists. If it doesn't, it create the folder.

    :param path: path to be selected
    :type path: str
    """
    if not file_folder_exists(path):
        os.makedirs(path)
    return path


class MySpider(CrawlSpider):
    name = 'gspider'
    allowed_domains = ['it.trustpilot.com']
    start_urls = [r'https://it.trustpilot.com']
    rules = (# Extract and follow all links!
        Rule(LinkExtractor(), callback='parse_item', follow=True), )
               
    def parse_item(self, response):
        if "review" in response.url:
            filename = f'{datetime.now().strftime("%Y%m%d%H%M%S%f")}.csv'
            outpath = select_or_create("data")
            time.sleep(10)
            myRev = scrapeTrustPilot(response.body)
            if len(myRev)>0:
                myRev.to_csv(os.path.join(outpath, filename))
        self.log('crawling'.format(response.url))
