from classes import Node, Connection

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, text):
        empty_node = Node.Node(text)

    def print_node (self):
        return empty_node.text

    """def add_edge(self, src, dest, srcPos, destPos):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.createGameEdge(srcPos, destPos)

    def createGameEdge(self, src, dest):
        edge = Connection.Connection(src, dest)"""
