class CrawlableGraph:
    def __init__(self, crawlables):
        self.crawlables = {
            crawlable
            for crawlable
            in crawlables
        }
