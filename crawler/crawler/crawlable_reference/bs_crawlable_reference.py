from crawler.crawlable_reference.crawlable_reference import CrawlableReference
from crawler.bs_crawlable_from import BsCrawlableFrom
from crawler.url import Url
import requests as rq


class BsCrawlableReference(CrawlableReference):
    def __init__(self, url=None):
        CrawlableReference.__init__(self)
        self.url = url

    def get(self):
        crawlable = BsCrawlableFrom.text(rq.get(self.url.text).text)
        crawlable.url = Url(self.url)
        return crawlable
