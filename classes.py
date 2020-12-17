class Cat:
    # name = 'Tom'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def eat(self):
        return f'{self.name} eats food'

    def __repr__(self):
        return f'Object of Cat Class'

    

if __name__ == "__main__":
    
    #instantiating Class or creating object
    cat1 = Cat('Tom', 'housecat')

    print(cat1)
    print(cat1.name)

    print(cat1.eat())

    cat2 = Cat('Snow White', 'russian')

    print(cat2.name)
    print(cat2.eat())


    print(cat1 + cat2)


    