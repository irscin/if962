from .crawlable import Crawlable
from .url import Url
from .bs_content import BsContent


class BsCrawlable(Crawlable):
    def __init__(self, anchors=list(), content=BsContent(), url=Url()):
        Crawlable.__init__(self, anchors, content, url)
