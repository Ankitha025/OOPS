from Animal import AbstractAnimal

class Cat(AbstractAnimal):
    def display_details(self):
        print("cat details:")
        print("breed:",self.breed)
        print("colour:",self.colour)
        print("number of legs:",self.num_legs)
        
class Dog(AbstractAnimal):
    def display_details(self):
        print("dog details:")
        print("breed:",self.breed)
        print("colour:",self.colour)
        print("number of legs:",self.num_legs)
        
class Fish(AbstractAnimal):
    def display_details(self):
        print("fish details:")
        print("breed:",self.breed)
        print("colour:",self.colour)
        print("number of legs:",self.num_legs)
                
class Bird(AbstractAnimal):
    def display_details(self):
        print("bird details:")
        print("breed:",self.breed)
        print("colour:",self.colour)
        print("number of legs:",self.num_legs)
                
        
        
        
    


