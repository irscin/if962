from crawler.crawlable_reference.crawlable_reference import CrawlableReference
from crawler.crawlable_from import CrawlableFrom
from download import UrlDownloader


class UrlCrawlableReference(CrawlableReference):
    def __init__(self, url=None, downloader=UrlDownloader()):
        self.url = url
        self.downloader = downloader

    def get(self):
        return CrawlableFrom.text(self.downloader.download_text(self.url))
