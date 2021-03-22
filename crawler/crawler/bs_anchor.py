from .anchor import Anchor


class BsAnchor(Anchor):
    def __init__(self, url=None, text='', bs=None):
        Anchor.__init__(self, url, text)
        self.bs = bs
