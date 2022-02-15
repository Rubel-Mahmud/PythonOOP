# Python Object oriented programing
# Simple inheritance


class Parant:

	def __init__(self):
		print("Init of Parant class")
		self.parant_name = 'parant name'



class Child(Parant):

	def __init__(self):
		print("Init of Child class")
		self.child_name = 'child name'
		super().__init__()




ch = Child()

print(ch.parant_name)

print(ch.child_name)