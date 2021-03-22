from .node_repository import NodeRepository
from .node import Node


class ListNodeRepository(NodeRepository):
    def __init__(self, nodes=list()):
        NodeRepository.__init__(self)
        self.nodes = nodes

    def add(self, node=Node()):
        self.nodes.append(node)

    def empty(self):
        return len(self.nodes) == 0

    def __contains__(self, item):
        return item in self.nodes

    def __iter__(self):
        return self.nodes.__iter__()
