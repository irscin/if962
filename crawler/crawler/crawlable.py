class Crawlable:
    def __init__(self, anchors=None, content=None):
        self.anchors = anchors
        self.content = content

    def get_anchors(self):
        return self.anchors

    def get_content(self):
        return self.content
