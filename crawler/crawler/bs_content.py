from .content import Content
import bs4


class BsContent(Content):
    def __init__(self, bs=bs4.BeautifulSoup):
        Content.__init__(self)
        self.bs = bs
