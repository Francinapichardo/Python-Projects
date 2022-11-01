import sqlite3


# Initialize first name
    
class Person:
  def __init__(self,  first_name, last_name= "Katherine",
               email="katherinel@gmail.com", password = "12345"):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = 12345

  def printname(self):
      print(self.first_name, self.last_name, self.email, self.password )

      

class Grades :
     print("Check your grades.")
      

class Student(Person):
    pass

  
 

#Use the Person class to create an object, and then execute the printname method:

x = Person("Katherine", "Linares")
x.printname()


