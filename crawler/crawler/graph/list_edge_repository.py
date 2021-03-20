from .edge_repository import EdgeRepository
from .edge import Edge


class ListEdgeRepository(EdgeRepository):
    def __init__(self, edges=list()):
        EdgeRepository.__init__(self)
        self.edges = edges

    def add(self, edge=Edge()):
        self.edges.append(edge)

    def __contains__(self, item):
        return item in self.edges
