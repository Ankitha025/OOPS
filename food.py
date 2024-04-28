class Bike:
    def __init__(self,name,cc):
        self.bike_name=name
        self.bike_cc=cc
    
    def Type(self):
        if self.bike_cc>200:
            print(f"{self.bike_name}is normal bike")
        else:
            print(f"{self.bike_name}is superbike")
            
Duke=Bike("RC390",390)
RE=Bike("Classic350",350)
Hero=Bike("Splender",110)

b=input("enter th bike: ")
if b=="Duke":
   print( Duke.Type()
elif b=="RE":
    RE.Type()
else:
    Hero.Type()
    
'''class Human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
            
    def display_info(self):
        print(f"he plays{self.fav_hobby},and he likes{self.fav_food}")
class Abcd(Human):
    def __init__(self,hobby,food,language):
        super().__init__(hobby,food)
        self.fav_language=language
    def display_info(self):
        super().display_info()
        print(f"language he speaks{self.fav_language}")
user=Abcd("games","biriyani","tamil")
user.display_info()'''
