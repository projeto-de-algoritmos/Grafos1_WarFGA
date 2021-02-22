from classes import Node
from tools import Places

class Player ():
	def __init__(self, name, decision, goals):
		self.name = name
		self.decision = decision
		self.goals = goals
		self.places = []
		self.nodeStudents = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	def add_classes(self, place):
		self.places.append(place)
		for i in range (42):
			if i == place:
				self.nodeStudents[i] = 1 

	def add_students(self, place):
		for i in range (42):
			if i == place:
				self.nodeStudents[i] = self.nodeStudents[i] + 1