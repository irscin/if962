from crawler.crawlable_reference.crawlable_reference import CrawlableReference
from crawler.bs_crawlable_from import BsCrawlableFrom
from crawler.url import Url
import requests as rq


class BsCrawlableReference(CrawlableReference):
    def __init__(self, url=Url(), base_url=Url()):
        CrawlableReference.__init__(self)
        self.url = url
        self.base_url = base_url

    def get(self):
        crawlable = BsCrawlableFrom.text(rq.get(self.url.text).text)
        crawlable.url = self.url
        return crawlable
