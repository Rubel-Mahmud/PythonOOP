# Python object oriented programing
# Property - getter - setter - deleter
# Celsius to Fahrenheit temprature


from numbers import Number


class Celsius:

	def __init__(self, temprature=0):
		# self.set_temprature(temprature)
		self._temprature = temprature


	# This method acting as a getter method
	@property
	def temprature(self):
		return self._temprature


	# This is setter method
	@temprature.setter
	def temprature(self, value):
		if isinstance(value, Number) and value >= -273:
			self._temprature = value
		else:
			self._temprature = 0		



	# This is deleter method
	@temprature.deleter
	def temprature(self):
		self._temprature = 0



	@property 
	def to_farenheit(self):
		return 1.8 * self.temprature + 32


	# def set_temprature(self, value):
	# 	if isinstance(value, Number) and value >= -273:
	# 		self._temprature = value
	# 	else:
	# 		self._temprature = 0


ob = Celsius(-392)

print(ob.temprature)

ob.temprature = -500

print(ob.temprature)
