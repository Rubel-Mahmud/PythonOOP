"""
In this class we will learn about 
class method, alternative constructor method and static class method

A class method is create using @classmethod decorator and take a object as argument called 'cls',
    the argument can be any name but standerd is cls
    a class method will access only class variable. it will not use instance variable
A alternative constructor is create using @classmethod decorator, it's actually a class method
A static class method is create using @staticmethod, static method don't access class variable or instance variable
"""

class Employee:

    # Class variable
    number_of_emp = 0

    raise_amount = 1.1


    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.number_of_emp += 1




    # Calculate Full name of a employee
    # This method will calculate fullname of a employee(an instance of the class Employee)
    # here self is refering the instance object as a perameter
    def fullname(self):
        name1 = self.first_name.title()
        name2 = self.last_name.lower()
        fullname = f'{name1} {name2}'
        # fullname = '{} {}'.format(self.first_name, self.last_name)
        return fullname



    # Calculate email address for each Employee instance
    # This method will take an instance as a peratmeter
    def email(self):
        name1 = self.first_name.lower()
        name2 = self.last_name.lower()
        email = f'{name1}.{name2}@company.com'
        if email.__contains__(' '):
            email = email.replace(' ', '')

        return email




    def apply_raise(self):

        # Without define a class variable, just hardcode it
        # In this way we can't change the value of salary increment
        # self.pay *= 1.1 
        self.pay *= self.raise_amount





    # Class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        print('Creating the class variable name = "Rubel" on the fly')
        cls.name = 'Rubel' # This will create a class bariable on the fly
        print('Created the class variable on the fly')



    # Alternative constructor method
    # This class method is using as a alternative constructor and returning a instance of the class
    @classmethod
    def from_string(cls, emp_string, delimiter='-'):
        f_name, l_name, pay = emp_string.split(delimiter)
        return cls(f_name, l_name, pay)



    # Static class method
    @staticmethod
    def is_worked(day):

        if day.weekday() in [5, 6]:
            print(day.weekday())
            return 'False'

        return 'True'



if __name__ == '__main__':

    # """This statements will for classmethod"""

    # print('Number of employee : ', Employee.number_of_emp)

    emp1 = Employee('Rubel', 'Mahmud', 5000)
    # emp2 = Employee('Rubel', 'ilma', 6000)

    # print('Before :')
    # print('Employee.raise_amount : ',Employee.raise_amount)
    # print('emp1.raise_amount : ',emp1.raise_amount)
    # print('emp2.raise_amount : ',emp2.raise_amount)

    # Employee.set_raise_amount(1.2) # Updating value of the class variable raise_amount, calling the method using Employee class
    # print()

    # print('After : calling Employee.set_raise_amount(1.2)')
    # print('Employee.raise_amount : ',Employee.raise_amount)
    # print('emp1.raise_amount : ',emp1.raise_amount)
    # print('emp2.raise_amount : ',emp2.raise_amount)

    # emp1.set_raise_amount(1.3) # Updating value of the class variable raise_amount, calling the method using Employee class
    # print()

    # print('After : calling emp1.set_raise_amount(1.3)')
    # print('Employee.raise_amount : ',Employee.raise_amount)
    # print('emp1.raise_amount : ',emp1.raise_amount)
    # print('emp2.raise_amount : ',emp2.raise_amount)


    # print()
    # print('Name : ', Employee.name)
    # print('Name : ', emp1.name)
    # print('Name : ', emp2.name)
    # print(Employee.__dict__)
    # print()
    # print(emp1.__dict__)
    # print()
    # print(emp2.__dict__)




    # """This statements will use for alternative constructor"""
    # str_1 = 'Rubel-Mahmud-5000' # This string for alternative constructor
    # str_2 = 'Rubel, M, 6000' # This string for alternative constructor
    # str_3 = 'Fatema | Ilma | 5000' # This string for alternative constructor

    # emp1 = Employee.from_string(str_1)
    # emp2 = Employee.from_string(str_2, delimiter=',')
    # emp3 = Employee.from_string(str_3, '|')

    # print(emp1.email())
    # print(emp2.email())
    # print(emp3.email())
    

    # # """This statements will use for staticmethod"""
    import datetime

    the_day = datetime.date(2022, 2, 6)

    print(the_day)

    print(Employee.is_worked(the_day))
    print('Instance : ',emp1.is_worked(the_day))

    # print('Number of employee : ', Employee.number_of_emp)

    # emp2 = Employee('Rubel', 'ilma', 6000)
    # print('Number of employee : ', emp1.number_of_emp)
