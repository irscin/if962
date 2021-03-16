from .crawlable_reference_with_anchor_meta_info_repository import CrawlableReferenceWithAnchorMetaInfoRepository


class SetCrawlableReferenceWithAnchorMetaInfoRepository(CrawlableReferenceWithAnchorMetaInfoRepository):
    def __init__(self, crawlable_references_with_anchor_meta_info=set()):
        CrawlableReferenceWithAnchorMetaInfoRepository.__init__(self, crawlable_references_with_anchor_meta_info)

    def __iter__(self):
        return self.crawlable_references_with_anchor_meta_info.__iter__()

    def __contains__(self, item):
        return self.crawlable_references_with_anchor_meta_info.__contains__(item)

    def add_all(self, new_crawlable_references_with_anchor_meta_info):
        self.crawlable_references_with_anchor_meta_info = {
            *self.crawlable_references_with_anchor_meta_info,
            *new_crawlable_references_with_anchor_meta_info
        }
