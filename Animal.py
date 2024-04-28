from abc import ABC,abstractmethod

class AbstractAnimal(ABC):
    def __init__(self,breed,colour,num_legs):
        self.breed=breed
        self.colour=colour
        self.num_legs=num_legs
        
    @abstractmethod
    def display_details(self):
            pass

