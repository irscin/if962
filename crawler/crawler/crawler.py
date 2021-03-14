class Crawler:
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def crawl(self):
        frontier = self.crawler_package.frontier
        chooser = self.crawler_package.frontier_item_chooser
        while not frontier.empty():
            next_crawlable_reference = chooser.choose_from(frontier)
            self.adjust_to_result(next_crawlable_reference)

    def adjust_to_result(self, crawlable_reference):
        pass
