from crawler import BsAnchor
from crawler import Url
from urllib.parse import urljoin
import bs4


class BsAnchorFrom:
    @staticmethod
    def bs(bs):
        return BsAnchor(
            text=bs.text,
            url=Url(bs['href']),
            bs=bs
        )

