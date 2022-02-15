# Python Object oriented programing
# Magic method


class Employee:

    number_of_emp = 0

    raise_amount = int(1.1)


    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.number_of_emp += 1


    def email(self):
        name1 = self.first_name.lower()
        name2 = self.last_name.lower()
        email = f'{name1}.{name2}@company.com'
        if email.__contains__(' '):
            email = email.replace(' ', '')

        return email



    def apply_raise(self):
        self.pay *= self.raise_amount



    # Python magic methods or special methods

    # This is string represantion method.
    def __str__(self):
    	return f'{self.first_name} {self.last_name} - {self.email()}'



    # This is also used for string represantion as alternative for __str__() method
    # When __str__() method and __repr__() method will have in same class at a time
    # then __str__() method will be used by default

    # def __repr__(self):
    # 	return f"Employee('{self.first_name}', '{self.last_name}', {self.pay})"



    # When two instance will add, this will return addition of their pay
    def __add__(self, other):
    	return self.pay + other.pay



    # This len method will call for an instance, it will return first_name and last_name length
    def __len__(self):
    	return len(self.first_name + self.last_name)



    # This will return True if all the property will equal, otherwise return False
    def __eq__(self, other):
    	if self.first_name == other.first_name and self.last_name == other.last_name and self.pay == other.pay:
    		return True
    	return False
    



if __name__ == '__main__':

	emp1 = Employee('Rubel', 'ilma', 30000)
	emp2 = Employee('Mahmud', 'ilma', 25000)
	emp3 = Employee('Mahmud', 'ilma', 25000)

	# print(emp1) # calling the __str__()

	# print(emp1 + emp2) # calling the __add__()

	# print(len(emp1)) # calling the __len__()

	print(emp3 == emp2)