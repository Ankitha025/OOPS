from Animal import Cat,Dog,Fish,Bird

def main():
    Cat=Cat(breed:"persian",colour:"white",number of legs:4)
    Dog=Dog(breed:"lab",colour:"cream",number of legs:4)
    Fish=Fish(breed:"starfish",colour:"pink",number of legs:0)
    Bird=Bird(breed:"parrot",colour:"parrot",number of legs:2)
    
    Cat.display_details()
    print("\n")
    Dog.display_details()
    print("\n")
    Fish.display_details()
    print("\n")
    Bird.display_details()
    
if __name__=="__main__":
   main()    




