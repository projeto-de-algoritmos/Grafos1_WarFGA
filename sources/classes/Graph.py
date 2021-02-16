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

    def add_edge(self, src, dest):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.createGameEdge(dest, src)
        print("Edge add from {0} to {1}".format(src.vertex, dest.vertex))

    def createGameEdge(self, dest, src):
        firstNode = None
        if (dest.vertex[0] == src.vertex[0]):
            if dest.vertex[1] < src.vertex[1]:
                firstNode = dest
            else:
                firstNode = src
            edge = Connection.Connection(32, 32, "vertical")
            edge.rect.x = firstNode.rect.x
            edge.rect.y = firstNode.rect.y + 18
        elif (dest.vertex[1] == dest.vertex[1]):
            if dest.vertex[0] < src.vertex[0]:
                firstNode = dest
            else:
                firstNode = src
            edge = Connection.Connection(32, 32, "horizontal")
            edge.rect.x = firstNode.rect.x + 18
            edge.rect.y = firstNode.rect.y

    def print_graph(self):
        for i in self.graph:
            print("{0}: {1}".format(i.vertex, self.graph[i]))
