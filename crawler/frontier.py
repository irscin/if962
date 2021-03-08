class Frontier:
    @staticmethod
    def for_crawlables(crawlables):
        frontier = Frontier()
        frontier.crawlable_graph = CrawlableGraph(crawlables)
        return frontier

    def __init__(self):
        self.crawlable_graph = None
