from .crawl_results import SinglePageResults
from .anchor_extractor import AnchorExtractor
from .content_extractor import ContentExtractor


class CrawlableConsumer:
    def __init__(
        self,
        anchor_extractor=AnchorExtractor(),
        content_extractor=ContentExtractor()
    ):
        self.anchor_extractor = anchor_extractor
        self.content_extractor = content_extractor

    def consume(self, crawlable):
        return SinglePageResults(
            anchors=self.anchors_from(crawlable),
            page_content=self.content_from(crawlable)
        )

    def anchors_from(self, crawlable):
        return self.anchor_extractor.extract_anchors(crawlable)

    def content_from(self, crawlable):
        return self.content_extractor.extract_content(crawlable)
