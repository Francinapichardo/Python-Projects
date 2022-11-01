# Parent Class User
from multiprocessing.dummy import Manager


class User:
    name = "Patricia"
    email = "Patricia@gmail.com"
    password = "1234567"

    def getLoginInfo(self):
        entry_name = input("Enter your name :")
        entry_email = input("Enter your email :")
        entry_password = input ("Enter your password:")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {} , let's start!".format(entry_name))
        else:
            print("The password and email is incorrect, try again.!") 

# Child class Employee
class Employe(User):
    base_pay = 20.00
    department = "Sales"
    pin_number = "1204"

#This is the same method in the parent class "User".
#The diference is that, instead of using entry_password, we are using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name :")
        entry_email = input("Enter your email :")
        entry_pin = input ("Enter your pin:")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {} , let's start!".format(entry_name))
        else:
            print("The pin and email is incorrect, try again.!") 

# The following code invokes code the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()
