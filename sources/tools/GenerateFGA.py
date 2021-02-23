from tools import Places


def createFGA():
    edges = []
    for node in Places.placesFGA:
        for neighbour in Places.placesFGA[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
            #priteLists.line_list.append((neighbour, node))
    return edges

def createALL():
    edges = []
    for node in Places.places:
        for neighbour in Places.places[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createUAC1():
    edges = []
    for node in Places.placesUAC1:
        for neighbour in Places.placesUAC1[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createUAC2():
    edges = []
    for node in Places.placesUAC2:
        for neighbour in Places.placesUAC2[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createUED():
    edges = []
    for node in Places.placesUED:
        for neighbour in Places.placesUED[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createRU():
    edges = []
    for node in Places.placesRU:
        for neighbour in Places.placesRU[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createPredioNovo():
    edges = []
    for node in Places.placesPredioNovo:
        for neighbour in Places.placesPredioNovo[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges

def createContainers():
    edges = []
    for node in Places.placesContainers:
        for neighbour in Places.placesContainers[node][1]:
            edges.append((node, neighbour))
            edges.append((neighbour, node))
    return edges