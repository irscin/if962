from .node_repository import NodeRepository
from .edge_repository import EdgeRepository
from .node import Node
from .edge import Edge


class Graph:
    def __init__(self, nodes=NodeRepository(), edges=EdgeRepository()):
        self.nodes = nodes
        self.edges = edges

    def add_node(self, node=Node()):
        self.nodes.add(node)

    def add_nodes(self, nodes=list()):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, edge=Edge()):
        self.edges.add(edge)

    def add_edges(self, edges=list()):
        for edge in edges:
            self.add_edge(edge)

    def edges_starting_with_one_of(self, nodes=NodeRepository()):
        return (edge for edge in self.edges if edge.first in nodes)

    def children_of(self, nodes=NodeRepository()):
        return (edge.second for edge in self.edges_starting_with_one_of(nodes))

    def empty(self):
        return self.nodes.empty()