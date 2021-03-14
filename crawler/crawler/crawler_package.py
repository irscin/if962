class CrawlerPackage:
    def __init__(
        self,
        frontier=None,
        frontier_item_choooser=None,
        crawlable_consumer=None
    ):
        self.frontier = frontier
        self.frontier_item_chooser = frontier_item_choooser
        self.crawlable_consumer = crawlable_consumer
