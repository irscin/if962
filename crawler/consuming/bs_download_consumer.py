from .crawlable_consumer import CrawlableConsumer
from crawler import BsCrawlable
from .path import Path


class BsDownloadConsumer(CrawlableConsumer):
    def __init__(self, path=Path()):
        CrawlableConsumer.__init__(self)
        self.path = path

    def consume(self, crawlable=BsCrawlable()):
        friendly_url = crawlable \
            .url \
            .text \
            .replace('http://', '') \
            .replace('/', ':')

        with open(self.path.path + friendly_url, 'w') as f:
            f.write(crawlable.content.bs)
