from .graph import BfsGraphIterable
from consuming import CrawlableConsumer


class CrawlerPackage:
    def __init__(
        self,
        frontier_item_consumer=BfsGraphIterable(),
        crawlable_consumer=CrawlableConsumer()
    ):
        self.frontier_item_consumer = frontier_item_consumer
        self.crawlable_consumer = crawlable_consumer
