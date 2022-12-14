

# parent class
class organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = " Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self) :
        msg = "\nName: ()\nspecies: ()\nLegs: ()\nDNA: ()\nOrigin: ()\Carbon Based: ()".format(self.name,self.species, self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
class Human (organism):
    name = 'MacGuyer'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin ='Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg


# another child class instance
    class Dog(organism):
        name = "Spot"
        species = 'canine'
        legs = 1
        arms = 0
        dna = "Sequence B"
        origin = 'Earth'

        def bite(self):
            msg = "\nEmits a loud, menancing growl and bites down ferociously on it's target!"
            return msg

# another child class instace
class Bacterium(organism):
        name = "X"
        species = 'Bacteria'
        legs = 0
        arms = 0
        dna = "Sequence C"
        origin = 'Mars'

        def replication(self):
            msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
            return msg
        




if __name__ == "__main__" :
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())

    

 
