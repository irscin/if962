from .graph import Graph
from .node import Node


class BfsGraphIterable:
    def __init__(self, graph=Graph(), initial_node=Node()):
        self.graph = graph
        self.initial_node = initial_node
        self.current_node = None
        self.left_nodes = list()
        self.right_nodes = list()
        self.sub_iterator = None

    def __iter__(self):
        self.current_node = None
        return self

    def __next__(self):
        if self.current_node is None:
            self.right_nodes = [self.initial_node]
            self.sub_iterator = self.right_nodes.__iter__()
            self.current_node = self.sub_iterator.__next__()
            return self.current_node
        else:
            return self._next_with_current_node()

    def _next_with_current_node(self):
        try:
            return self.sub_iterator.__next__()
        except StopIteration:
            self.left_nodes = self.right_nodes
            self.right_nodes = set(self.graph.children_of(self.left_nodes))
            self.sub_iterator = self.right_nodes.__iter__()
            return self.sub_iterator.__next__()
