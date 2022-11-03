class Protected:
    # Sets variable to 12 and creates a protected variable set to 0.
    def __init__(self):
        self.__privateVar = 12
        self._protectedVar = 0

    def getPrivate(self):  # Prints out the private variable.
        print(self.__privateVar)

    # Sets the private variable to be a new value.
    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()  # set obj to call the class Protected
obj.getPrivate()  # gets the original private value
obj._protectedVar = 34
print(obj._protectedVar)
obj.setPrivate(23)
obj.getPrivate()
