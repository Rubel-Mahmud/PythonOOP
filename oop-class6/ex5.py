# Python Object oriented programing
# Multiple inheritance / Triple inheritance
# Passing parameter, *args, **kwargs
# There has nothing to think, maximum thing here is rules of python oop



class First:

	def __init__(self, f, name, **kwargs):
		print("Init of First class")
		self.f = f
		self.name = name
		super().__init__(**kwargs)



class Second:

	def __init__(self, s, **kwargs):
		print("Init of Second class")
		self.s = s
		super().__init__(**kwargs)



class Third:

	def __init__(self, t, **kwargs):
		print("Init of Third class")
		self.t = t
		super().__init__(**kwargs)



class Combined(First, Second, Third):

	def __init__(self, f, s, t, name):

		print("Init of Combined class")

		super().__init__(f=f, s=s, t=t, name=name) # Calling all the classes in one statement



ch = Combined('First', 'Second', 'Third', 'Rubel')


print(ch.f, ch.s, ch.t)
print(ch.name)