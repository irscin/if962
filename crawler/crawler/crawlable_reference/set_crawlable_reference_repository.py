from .crawlable_reference_repository import CrawlableReferenceRepository


class SetCrawlableReferenceRepository(CrawlableReferenceRepository):
    def __init__(self, crawlable_references=set()):
        CrawlableReferenceRepository.__init__(self, crawlable_references)

    def __iter__(self):
        return self.crawlable_references.__iter__()

    def __contains__(self, item):
        return self.crawlable_references.__contains__(item)

    def add_all(self, new_crawlable_references):
        self.crawlable_references = {*self.crawlable_references, *new_crawlable_references}
