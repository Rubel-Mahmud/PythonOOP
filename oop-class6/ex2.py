# Python Object oriented programing
# Multiple inheritance / Double inheritance


class Father:

	def __init__(self):
		print("Init of Father class")



class Mother:

	def __init__(self):
		print("Init of Mother class")



# Here the super() method calling only the Father class __init__()
# class Child(Father, Mother):

# 	def __init__(self):
# 		print("Init of Child class")

# 		super().__init__()



# Here the super() method calling only the Mother class __init__()
# class Child(Mother, Father):

# 	def __init__(self):
# 		print("Init of Child class")

# 		super().__init__()



# # Here the super() method calling Father and Mother class __init__()
# class Child(Father, Mother):

# 	def __init__(self):
# 		print("Init of Child class")

# 		super().__init__() # This will call Father class
# 		super(Father, self).__init__() # This will call Mother class




# # Here the super() method calling Father and Mother class __init__()
# class Child(Father, Mother):

# 	def __init__(self):
# 		print("Init of Child class")

# 		Father.__init__(self)
# 		Mother.__init__(self)


ch = Child()
