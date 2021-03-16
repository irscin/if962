from crawler import BsAnchor
from crawler import Url


class BsAnchorFrom:
    @staticmethod
    def bs(bs):
        return BsAnchor(
            text=bs.text,
            url=Url(bs['href']),
            bs=bs
        )
