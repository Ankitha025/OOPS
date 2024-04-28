from Animal import Cat,Dog,Fish,Bird

def main():
    cat=Cat("persian","white",4)
    dog=Dog("lab","cream",4)
    fish=Fish("starfish","pink",0)
    bird=Bird("parrot","parrot",2)
    
    cat.display_details()
    print("\n")
    dog.display_details()
    print("\n")
    fish.display_details()
    print("\n")
    bird.display_details()
    
if __name__=="__main__":
   main()    




