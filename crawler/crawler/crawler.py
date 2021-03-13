class Crawler:
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package

    def crawl(self):
        frontier = self.crawler_package.frontier
        chooser = self.crawler_package.frontier_item_chooser
        while not frontier.empty():
            crawl_result = self.consume(chooser.choose_from(frontier).get())
            self.adjust_to_result(crawl_result)

    def consume(self, crawlable):
        return self.crawler_package.crawlable_consumer.consume(crawlable)