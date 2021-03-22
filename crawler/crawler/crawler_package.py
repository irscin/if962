from .graph import BfsGraphIterable, Graph
from consuming import CrawlableConsumer


class CrawlerPackage:
    def __init__(
        self,
        graph=Graph(),
        frontier_item_consumer=BfsGraphIterable(),
        crawlable_consumer=CrawlableConsumer()
    ):
        self.graph = graph
        self.frontier_item_consumer = frontier_item_consumer
        self.crawlable_consumer = crawlable_consumer
