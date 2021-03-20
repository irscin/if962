from .crawler_package import CrawlerPackage


class Crawler:
    def __init__(self, crawler_package=CrawlerPackage()):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def crawl(self):
        consumer = self.crawler_package.frontier_item_consumer
        for crawlable_reference_node in consumer:
            self.adjust_to_result(crawlable_reference_node)

    def adjust_to_result(self, crawlable_reference_node):
        pass
