from .crawler import Crawler
from crawler.crawlable_reference.bs_crawlable_reference import BsCrawlableReference
from crawler.crawlable_reference.meta.crawlable_reference_with_anchor_meta_info import CrawlableReferenceWithAnchorMetaInfo
from crawler.crawlable_reference.meta.bs_anchor_meta_info import BsAnchorMetaInfo


class OnePassCrawler(Crawler):
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def adjust_to_result(self, crawlable_reference_with_anchor_meta_info):
        frontier = self.crawler_package.frontier

        current_url = crawlable_reference_with_anchor_meta_info.crawlable_reference.url
        crawlable = crawlable_reference_with_anchor_meta_info.crawlable_reference.get()

        new_crawlable_references_with_anchor_meta_info = {
            CrawlableReferenceWithAnchorMetaInfo(
                crawlable_reference=BsCrawlableReference(bs_anchor.url),
                anchor_meta_info=BsAnchorMetaInfo(
                    bs_parent=bs_anchor.bs.parent,
                    bs_in=bs_anchor.bs
                )
            )
            for bs_anchor
            in crawlable.get_anchors()
        }

        frontier.add_all(
            filter(
                lambda cr: not self.references_visited_url(cr),
                new_crawlable_references_with_anchor_meta_info
            )
        )

        self.visited_urls.add(current_url)

    def references_visited_url(self, crawlable_reference_with_anchor_meta_info):
        return crawlable_reference_with_anchor_meta_info \
            .anchor_meta_info \
            .bs_in['href'] in self.visited_urls
