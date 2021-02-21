# key: country, (x,y), (width, height), [connected keys]
places = {
    # UED primeiro andar
    0: ("LabEletronica", (45, 38), (125, 25), [1, 2, 3]),
    1: ("LabDoAC", (170, 38), (125, 25), [0, 3, 4]),
    2: ("LabFis", (45, 63), (84, 25), [0, 3]),
    3: ("LabEletricidade", (129, 63), (83, 25), [0, 1, 2, 4]),
    4: ("Mocap", (212, 63), (83, 25), [1, 3]),
    # UED segundo andar
    5: ("Coordenação", (45, 106), (125, 25), [1, 2]),
    6: ("Sala Professor 1", (170, 106), (125, 25), [0, 3]),
    7: ("Sala Professor 2", (45, 131), (125, 25), [0, 3]),
    8: ("Sala Professor 3", (170, 131), (125, 25), [1, 2]),
    # UAC primeiro andar
    9: ("I01", (536, 15), (41, 112), [10]),
    10: ("I02", (577, 15), (41, 112), [9, 11]),
    11: ("I03", (618, 15), (41, 112), [10, 12]),
    12: ("I04", (659, 15), (41, 112), [11, 13]),
    13: ("I05", (700, 15), (40, 112), [12, 14]),
    14: ("I06", (740, 15), (40, 112), [13]),
    # UAC segundo andar
    15: ("S01", (536, 127), (35, 111), [16]),
    16: ("S02", (571, 20), (35, 111), [15, 17]),
    17: ("S03", (606, 20), (35, 111), [16, 18]),
    18: ("S04", (641, 20), (35, 111), [17, 19]),
    19: ("S05", (676, 20), (35, 111), [18, 20]),
    20: ("S06", (711, 20), (35, 111), [19, 21]),
    21: ("S07", (746, 20), (34, 111), [20]),
    # Containers
    24: ("Container1", (150, 218), (122, 188), [25, 26]),
    25: ("Container2", (272, 218), (122, 94), [24]),
    26: ("Container3", (272, 312), (122, 94), [24]),
    # Predio Novo
    27: ("Lab1", (250, 430), (100, 75), [2, 3]),
    28: ("Lab2", (350, 430), (100, 75), [1, 4]),
    29: ("Lab3", (250, 505), (100, 75), [1, 4]),
    30: ("Lab4", (350, 505), (100, 75), [2, 3]),
    # RU
    30: ("Mamutes do Cerrado", (550, 450), (156, 45), []),
    31: ("DAEng", (550, 495), (52, 45), []),
    32: ("Sala Múltimidia", (602, 495), (52, 45), []),
    33: ("FGARacing", (654, 495), (52, 45), []),
}
