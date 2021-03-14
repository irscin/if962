from .crawler import Crawler
from .bs_crawlable_reference import BsCrawlableReference
from .url import Url


class OnePassCrawler(Crawler):
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def adjust_to_result(self, crawlable_reference):
        frontier = self.crawler_package.frontier

        current_url = crawlable_reference.url
        crawlable = crawlable_reference.get()

        new_crawlable_references = {
            BsCrawlableReference(anchor.url)
            for anchor
            in crawlable.get_anchors()
        }

        frontier.add_all(
            filter(
                lambda cr: not self.references_visited_url(cr),
                new_crawlable_references
            )
        )

    def references_visited_url(self, crawlable_reference):
        return crawlable_reference.url in self.visited_urls
