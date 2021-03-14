from crawler.crawlable_reference import CrawlableReference
from crawler.crawlable_from import CrawlableFrom
import requests as rq


class BsCrawlableReference(CrawlableReference):
    def __init__(self, url=None):
        CrawlableReference.__init__(self)
        self.url = url

    def get(self):
        return CrawlableFrom.text(rq.get(self.url.text))
