from .url import Url


class Crawlable:
    def __init__(self, anchors=None, content=None, url=Url()):
        self.anchors = anchors
        self.content = content
        self.url = url

    def get_anchors(self):
        return self.anchors

    def get_content(self):
        return self.content

    def get_url(self):
        return self.url
