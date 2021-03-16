from .bs_crawlable_reference import BsCrawlableReference


class BsCrawlableReferenceFrom:
    @staticmethod
    def anchor(anchor):
        return BsCrawlableReference(anchor.url)
