from tools import FGAMap


def createTable(graph):
    for i in FGAMap.places:
        node = graph.add_node(
            FGAMap.places[i][2][0], FGAMap.places[i][2][1], FGAMap.places[i][1][0], FGAMap.places[i][1][1], FGAMap.places[i][0], 12)
