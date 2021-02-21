#nome
#Ásia, 12 países
placesUAC1 = {
	1: ("Biblioteca", [3, 7, 'b']),
	2: ("Auditório Baixo", [5, 'c']),
	3: ("Escadas 1.1", [1, 7]),
	4: ("Escadas 2.1", [8, 9, 'a', 'b']),
	5: ("Mesinhas", [2, 12]),
	6: ("O Belisco", [7, 12]),
	7: ("Secretaria", [1, 3, 6]),
	8: ("WC F", [4, 9, 'a', 'b']),
	9: ("WC M", [4, 8, 'a', 'b']),
	'a': ("Salas comput.", [4, 8, 9]),
	'b': ("Salas de aulas", [1, 4, 8, 9]),
	'c': ("Entrada", [2, 5, 6, 'c'])
}

#América do Norte, 9 países
placesUAC2 = {
	1: ("Auditorio Cima", [2, 5]),
	2: ("Mesas auditorio", [1, 5]),
	3: ("Banheiro S01", [5, 6, 8]),
	4: ("Banheiros S10", [7, 9]),
	5: ("Sala psicológico", [1, 2, 3, 8]),
	6: ("Salas de aulas", [1, 3, 5, 9]),
	7: ("Sala S10", [4, 9]),
	8: ("Escadas 1.2", [3, 5, 6]),
	9: ("Escadas 2.2", [4, 6, 7])
}

#Europa, 7 países
placesUED = {
	1: ("Lab.Fís.Exp.", [4, 5, 7]),
	2: ("Lab.Quim.Exp.", [3, 6]),
	3: ("MOCAP", [2, 6]),
	4: ("Lab.PED1", [1, 5, 6]),
	5: ("Mesas Amarelas", [1, 4, 7]),
	6: ("Entrada Portão", [2, 3, 4, 7]),
	7: ("Entrada Containers", [1, 5, 6])
}

#África, 6 países
placesRU = {
	1: ("Mesas", [2, 6]),
	2: ("Lugar de se servir", [1, 6]),
	3: ("UNBaja", [1, 5]),
	4: ("DAEng", [3, 5, 6]),
	5: ("Sala Multimidia", [3, 4]),
	6: ("Mamutes do Cerrado", [1, 2, 4])
}

#Oceania, 4 países
placesPredioNovo = {
	1: ("Entrada", [2, 3, 4]),
	2: ("Sala 02", [1, 3, 4]),
	3: ("Sala 03", [1, 2, 4]),
	4: ("Sala 04", [1, 2, 3])
}

#América do Sul, 4 países
placesContainers = {
	1: ("Empresas Júnior's", [2, 3, 4]),
	2: ("Container 1", [1, 3, 4]),
	3: ("Container 2", [1, 2, 4]),
	4: ("Container 3", [1, 2, 3])
}

placesFGA = {
	1: ("UAC 1º andar", [2, 3, 4]),
	2: ("UAC 2º andar", [1]),
	3: ("UED",[1, 4, 6]),
	4: ("RU", [1, 4, 5]),
	5: ("Prédio novo", [4]),
	6: ("Containers", [3])
}

places = {
	#UAC 1º andar
	1: ("Biblioteca", [3, 7, 11]),
	2: ("Auditório Baixo", [5, 12, 13]),
	3: ("Escadas 1.1", [1, 7, 20]),
	4: ("Escadas 2.1", [8, 9, 10, 11, 21]),
	5: ("Mesinhas", [2, 12]),
	6: ("O Belisco", [7, 12]),
	7: ("Secretaria", [1, 3, 6]),
	8: ("WC F", [4, 9, 10, 11]),
	9: ("WC M", [4, 8, 10, 11]),
	10 : ("Salas comput.", [4, 8, 9]),
	11: ("Salas de aulas", [1, 4, 8, 9]),
	12 : ("Entrada", [2, 5, 6, 27, 29, 33]),

	#UAC 2º andar
	13: ("Auditorio Cima", [2, 14, 17]),
	14: ("Mesas auditorio", [13, 17]),
	15: ("Banheiro S01", [17, 18, 20]),
	16: ("Banheiros S10", [19, 21]),
	17: ("Sala psicológico", [13, 14, 15, 20]),
	18: ("Salas de aulas", [13, 15, 5, 21]),
	19: ("Sala S10", [16, 21]),
	20: ("Escadas 1.2", [3, 15, 17, 18]),
	21: ("Escadas 2.2", [4, 16, 18, 19]),

	#UED
	22: ("Lab.Fís.Exp.", [25, 26, 28]),
	23: ("Lab.Quim.Exp.", [24, 27]),
	24: ("MOCAP", [23, 27]),
	25: ("Lab.PED1", [22, 26, 27]),
	26: ("Mesas Amarelas", [22, 25, 28]),
	27: ("Entrada Portão", [12, 23, 24, 25, 28]),
	28: ("Entrada Containers", [22, 26, 27, 39, 42]),

	#RU
	29: ("Mesas", [12, 30, 34]),
	30: ("Lugar de se servir", [29, 34]),
	31: ("UNBaja", [29, 33, 35]),
	32: ("DAEng", [31, 33, 34, 35]),
	33: ("Sala Multimidia", [12, 31, 32,35]),
	34: ("Mamutes do Cerrado", [29, 30, 32]),

	#Prédio Novo
	35: ("Entrada", [31, 32, 33, 36, 37, 38]),
	36: ("Sala 02", [35, 37, 38]),
	37: ("Sala 03", [35, 36, 38]),
	38: ("Sala 04", [35, 36, 37]),

	#Containers
	39: ("Empresas Júnior's", [28, 40, 41, 42]),
	40: ("Container 1", [39,41, 42]),
	41: ("Container 2", [39, 40, 42]),
	42: ("Container 3", [28, 39, 40, 41])
}