import sqlite3

conn = sqlite3.connect('test.db')

class User:
    #Define the attributes of the class
    name = "Francina"
    email = "francinap@gmail.com"
    password = "abcdeg"
    account_number = 0



    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password; ")
        if (entry_email == self.email and entry_password == self.password) :
            print("Welcome back {}".format(self.name))
        else:
            print("You are not authorizided for this page.")
#Outside od the class you would create an instance of the User class
new_user = User()
#Call the login method using the new object
new_user.login()

def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account =account

