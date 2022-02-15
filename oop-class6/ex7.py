# Python object oriented programing
# Class and Inner class/ Nested class



class Color:

	def __init__(self):
		self.__what_is_color()
		# self.red = self.Red() # Creating subclass instance to access subclass as like property


	# This method is for access the subclass Red as like property
	# Example : ob.red.color_name, ob.red.color_code
	@property
	def red(self):
		return self.Red()


	@property
	def green(self):
		return self.Green()


	class Red:
		
		def __init__(self):
		    self.__color_name = 'Red'
		    self.__color_code = 'ff0000'


		@property
		def color_name(self):
		    return self.__color_name


		@property
		def color_code(self):
		    return self.__color_code



	class Green:
		
		def __init__(self):
		    self.__color_name = 'Green'
		    self.__color_code = 'unknown'


		@property
		def color_name(self):
		    return self.__color_name


		@property
		def color_code(self):
		    return self.__color_code




	@property
	def what_is_color(self):
		return self.__what_is_color


	@property
	def color_attributes(self):
		return self.__color_attributes



	def __what_is_color(self):

		self.__what_is_color = """Color or colour is the visual perceptual property 
		corresponding in humans to the categories called blue, green, red, etc. 
		Color derives from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors"""

		self.__color_attributes = 'Brightness', 'Saturation', 'Hue' # This is a tuple




ob = Color()

# obr = ob.Red() # Creating sub class instance

# print(ob.Red()._Red__color_name) # This is data hiding  
# print(ob.Red()._Red__color_code) # Data hiding

# ob.red = None # After this statement subclass instance will not work as like property

print(ob.red.color_name)
print(ob.red.color_code)

print()

print(ob.green.color_name)
print(ob.green.color_code)