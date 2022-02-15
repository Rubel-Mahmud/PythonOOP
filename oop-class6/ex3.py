# Python Object oriented programing
# Multiple inheritance / Triple inheritance


class First:

	def __init__(self):
		print("Init of First class")



class Second:

	def __init__(self):
		print("Init of Second class")


class Third:

	def __init__(self):
		print("Init of Third class")



class Combined(First, Second, Third):

	def __init__(self):

		print("Init of Combined class")

		super().__init__()
		super(First, self).__init__() # Calling the second class
		super(Second, self).__init__() # Calling the third class


ch = Combined()
