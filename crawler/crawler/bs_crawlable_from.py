import bs4
from .bs_crawlable import BsCrawlable
from .bs_content import BsContent
from reading import BsAnchorFrom
from crawler import Url


class BsCrawlableFrom:
    @staticmethod
    def text(text=''):
        bs = bs4.BeautifulSoup(text, features="html5lib")
        return BsCrawlable(
            anchors={BsAnchorFrom.bs(bs_anchor) for bs_anchor in bs.find_all('a', href=True)},
            content=BsContent(bs)
        )

