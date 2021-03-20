from .graph import Graph


class CrawlerPackage:
    def __init__(
        self,
        frontier=Graph(),
        frontier_item_chooser=None,
        crawlable_consumer=None
    ):
        self.frontier = frontier
        self.frontier_item_chooser = frontier_item_chooser
        self.crawlable_consumer = crawlable_consumer
