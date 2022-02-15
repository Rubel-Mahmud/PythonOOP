

class Employee:

    # This is python constructor method
    # (simply a function that used to initialize values
    # during create an instance of the class Employee
    # Here self is a perameter that refering the instance object
    # the perameter self can be any name.."rahim, korim, jodu, modu but standered is self"
    # self.first_name means creating a property to the referd instance
    # Note : when you create an instance of any class, the self perameter is automatically passed to the __init_constructor
    # To check this just run a constructor without the self perameter

    # def __init__():
    #     pass

    # def __init__(obj, first_name, last_name):
    #     obj.first_name = first_name
    #     obj.last_name = last_name

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




if __name__ == '__main__':
    emp1 = Employee('Rubel', 'Mahmud', 5000)
    emp2 = Employee('Fatema akhter', 'Ilma', 6000)


    # emp1.first_name = 'Rubel'
    # emp2.first_name = 'Fatema akhter'
    # emp1.last_name = 'Mahmud'
    # emp2.last_name = 'Ilma'

    print(emp1.first_name)
    print(emp1.last_name)
    print(emp1.pay)
    print('Fullname :', emp1.fullname())
    print('Email :', emp1.email())
    print()
    print(emp2.first_name)
    print(emp2.last_name)
    print(emp2.pay)
    print('Fullname :',emp2.fullname())
    print('Email :',emp2.email())