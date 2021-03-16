import bs4
from .bs_crawlable import BsCrawlable
from .bs_content import BsContent
from reading import AnchorFrom


class BsCrawlableFrom:
    @staticmethod
    def text(text=''):
        bs = bs4.BeautifulSoup(text)
        return BsCrawlable(
            anchors={AnchorFrom.bs(bs_anchor) for bs_anchor in bs.find_all('a')},
            content=BsContent(bs)
        )
