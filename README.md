# trustpilot_spider
A spider to get reviews and stars from trustpilot. I wrote this code in order to build an NLP dataset for sentiment analysis in Italian.

## Prerequisites

This script depends on the module TrustpilotScraper and Scrapy, you can download and install them with:

```python
pip install git+https://github.com/AlessandroGianfelici/trustpilot_scraper.git

pip install scrapy
```

## Usage 

In the root folder run the command:

```python
scrapy runspider myspider.py
```


