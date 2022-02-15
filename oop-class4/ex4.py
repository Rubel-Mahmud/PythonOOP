# Python object oriented programing
# Inheritance - Subclass creating

class Employee:

    number_of_emp = 0

    raise_amount = int(1.1)


    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.number_of_emp += 1



    def fullname(self):
        name1 = self.first_name.title()
        name2 = self.last_name.lower()
        fullname = f'{name1} {name2}'
        return fullname



    def email(self):
        name1 = self.first_name.lower()
        name2 = self.last_name.lower()
        email = f'{name1}.{name2}@company.com'
        if email.__contains__(' '):
            email = email.replace(' ', '')

        return email



    def apply_raise(self):
        self.pay *= self.raise_amount




class Developer(Employee):
	
	raise_amount = 2.5

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.base_lang = prog_lang




class Manager(Employee):

	def __init__(self, first_name, last_name, pay, employee=None):
		self.employees = []
		super().__init__(first_name, last_name, pay)

		if employee not in self.employees:
			self.employees.append(employee)



	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)


	def rem_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)




if __name__ == '__main__':
	
	# Creating developer instance
	dev1 = Developer('Rubel', 'ilma', 30000, 'Python')
	dev2 = Developer('Mahmud', 'ilma', 20000, 'Java')

	man1 = Manager('Ilma', 'Mahmud', 25000)

	print(dev1.first_name)

	print(man1.first_name)

	print('Totall employees : ', len(man1.employees))

	# print(man1.employees[0].first_name)

	man1.add_emp(dev2)

	print('Totall employees : ', len(man1.employees))

	# print(man1.employees[0].first_name)
	# print(man1.employees[1].first_name)

	man1.rem_emp(dev2)

	print('Totall employees : ', len(man1.employees))


