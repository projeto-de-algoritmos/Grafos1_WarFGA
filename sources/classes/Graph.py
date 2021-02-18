from classes import Node, Connection


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, width, height, posX, posY, text, textSize):
        empty_node = Node.Node(width, height, text, textSize)
        empty_node.rect.x = posX
        empty_node.rect.y = posY
        self.graph[empty_node] = []
        return empty_node

    def add_edge(self, src, dest, srcPos, destPos):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.createGameEdge(srcPos, destPos)

    def createGameEdge(self, src, dest):
        edge = Connection.Connection(src, dest)

    def print_graph(self):
        for i in self.graph:
            print("{0}: {1}".format(i.vertex, self.graph[i]))
