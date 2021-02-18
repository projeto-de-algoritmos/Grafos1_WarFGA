from tools import FGAMap


def createTable(graph):
    nodes = []
    for i in FGAMap.places:
        nodes.append(graph.add_node(
            FGAMap.places[i][2][0], FGAMap.places[i][2][1], FGAMap.places[i][1][0], FGAMap.places[i][1][1], FGAMap.places[i][0], 12)
        )
    count = 0
    for i in nodes:
        for j in (FGAMap.places[count][3]):
            graph.add_edge(
                i, nodes[j], FGAMap.places[count][4], FGAMap.places[j][4])
        count = count + 1
