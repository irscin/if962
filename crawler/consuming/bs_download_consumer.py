from .crawlable_consumer import CrawlableConsumer
from .namer import Namer
from .path import Path
from crawler import BsCrawlable


class BsDownloadConsumer(CrawlableConsumer):
    def __init__(self, path=Path(), namer=Namer()):
        CrawlableConsumer.__init__(self)
        self.path = path
        self.namer = namer

    def consume(self, crawlable=BsCrawlable()):
        name = self.namer.name_crawlable(crawlable)

        with open(self.path.path + name, 'w') as f:
            f.write(f'{crawlable.url.text}\n{str(crawlable.content.bs)}')
