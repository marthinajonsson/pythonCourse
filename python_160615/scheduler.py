class Schedule:
	def __init__(self):
		self.slots = []
	def book(self, name):
		self.slots.append(name)
		print("Booked: ", name)

s = Schedule()
s.book("appointment 1")

