from .crawlable import Crawlable


class BsCrawlable(Crawlable):
    def __init__(self, anchors=None, content=None):
        self.anchors = anchors
        self.content = content
