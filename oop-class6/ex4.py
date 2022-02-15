# Python Object oriented programing
# Multiple inheritance / Triple inheritance


class First:

	def __init__(self):
		print("Init of First class")
		super().__init__()



class Second:

	def __init__(self):
		print("Init of Second class")
		super().__init__()



class Third:

	def __init__(self):
		print("Init of Third class")
		super().__init__()



class Combined(First, Second, Third):

	def __init__(self):

		print("Init of Combined class")

		super().__init__() # Calling all the classes in one statement



ch = Combined()
