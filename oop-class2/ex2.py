"""
In this class we will learn about class variable 
in onther word it's global variable

A class variable can be define inside a class
A class variable have to access via instance object or classname
Example : self.class_variable_name or class_name.class_variable_name
Like : self.raise_amount or Employee.raise_amount
"""

class Employee:

    # Class variable
    raise_amount = 1.1


    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay




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



if __name__ == '__main__':
    emp1 = Employee('Rubel', 'Mahmud', 5000)
    emp2 = Employee('Rubel', 'ilma', 6000)

    print(emp1.pay) # Before appling the apply_raise() method
    
    
    emp1.raise_amount = 1.2 
    # this will create a instance variable named raise_amount. 
    # It's not change the class variable raise_amount
    # To check this is true just replace the self.pay *= self.raise_amount with self.pay *= Employee.raise_amount
    # And run the below command
    # See that in emp1.__dict__ has created a instance variable called raise_amount with value 1.2
    # emp2.__dict__ has no instance variable called raise_amount
    # Employee.__dict__ has the raise_amount with the initial value 1.1

    print(emp1.__dict__)
    print()
    print(Employee.__dict__)
    print()
    print(emp2.__dict__)



    emp1.apply_raise() # Appling the apply_raise() method

    print(emp1.pay) # After appling the apply_raise() method
