from .edge import Edge


class DirectedEdge(Edge):
    def __init__(self, origin=None, destination=None):
        Edge.__init__(origin, destination)
        self.origin = origin
        self.destination = destination
