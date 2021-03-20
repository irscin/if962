class Path:
    def __init__(self, path=''):
        self.path = path

    def __add__(self, other):
        return Path(self.path + other.path)
