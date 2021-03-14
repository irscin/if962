from crawler import Anchor
from crawler import Url


class AnchorFrom:
    @staticmethod
    def bs(bs):
        return Anchor(
            text=bs.text,
            url=Url(bs['href'])
        )
