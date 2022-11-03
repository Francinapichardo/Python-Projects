import sqlite3


# Initialize first name

class Person:
    def __init__(self,  first_name="Katherine", last_name="Linares",
                 email="katherinel@gmail.com", password="12345"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = 12345

    def printname(self):
        print(self.first_name, self.last_name, self.email, self.password)


class Grades:
      minimum_passing = 65
      def __init__(self,score):
          self.score = score
          def is_passing(self,score):
            self.score = score
            if self.score>=Grade.minimum_passing:
                return True
            else:
                return False

                

class Student(Person):
    def __init__(self, first_name, last_name, year = "2013"):
        self.graduationyear = 2013


# Use the Person class to create an object, and then execute the printname method:
if __name__ == "__main__":
    x = Person("Katherine", "Linares")
    x = Student("Katherine", "Linares, 2013")
    x.printname()

