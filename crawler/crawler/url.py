class Url:
    def __init__(self, text=''):
        self.text = text

    def __equals__(self, other):
        return self.text == other.text
