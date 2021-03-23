from .namer import Namer
from crawler import Crawlable


class CounterNamer(Namer):
    def __init__(self):
        self.counter = 0

    def name_crawlable(self, crawlable=Crawlable()):
        self.counter += 1
        return f'{self.counter}.myhtml'