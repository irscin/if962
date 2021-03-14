from .crawlable import Crawlable
from .content import Content
from reading import AnchorFrom
import bs4


class CrawlableFrom:
    @staticmethod
    def text(text=''):
        bs = bs4.BeautifulSoup(text)
        return Crawlable(
            anchors={AnchorFrom.bs(bs_anchor) for bs_anchor in bs.find_all('a')},
            content=Content(text=bs.text)
        )
