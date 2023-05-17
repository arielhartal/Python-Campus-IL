class Animal:

    def __init__(self, name, hunger = 0):
        self._name = name
        self._hunger = hunger


    def set_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Skunk(Animal):
    pass

class Unicorn(Animal):
    pass

class Dragon(Animal):
    pass



def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst.extend(dog, cat, skunk, unicorn, dragon)

main()