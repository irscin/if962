from .content import Content


class BsContent(Content):
    def __init__(self, bs=None):
        super.__init__(self)
        self.bs = bs