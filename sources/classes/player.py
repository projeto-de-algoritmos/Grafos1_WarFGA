from classes import Node
from tools import Places

class Player ():
	def __init__(self, name, decision, goals):
		self.name = name
		self.decision = decision
		self.goals = goals
		self.places = []
		self.nodeStudents = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

	def add_classes(self, place):
		self.places.append(place)

	def rmv_classes(self, place):
		tam = len(self.places)
		for i in range(0, tam-1):
			if self.places[i] == place:
				self.places.pop(i)
	
	def add_students(self, place):
		for i in range (42):
			if i == place:
				self.nodeStudents[i] = self.nodeStudents[i] + 1

	def rmv_students(self, place):
		for i in range (42):
			if i == place:
				self.nodeStudents[i] = self.nodeStudents[i] - 1

	def qtdStudents(self, place):
		for i in range (42):
			if i == place:
				return self.nodeStudents[i]
