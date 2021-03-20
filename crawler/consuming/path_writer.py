from .path import Path


class PathWriter:
    def __init__(self, path=Path()):
        self.path = path

    def write(self, to_write=''):
        with open(self.path.path, 'w') as f:
            f.write(to_write)
