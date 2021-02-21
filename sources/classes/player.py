class Player ():
	def __init__(self, name, decision, goals):
		self.name = name
		self.decision = decision
		self.goals = goals
		self.places = []

	def add_classes(self, place):
		self.places.append(place)
