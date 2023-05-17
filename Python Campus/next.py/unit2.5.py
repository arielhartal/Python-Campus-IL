class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger = 0,):
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


    def talk(self):
        if type(self).__name__ == "Dog" :
            print("woof woof")

        if type(self).__name__ == "Cat" :
            print("meow")

        if type(self).__name__ == "Skunk" :
            print("tsssss")

        if type(self).__name__ == "Unicorn" :
            print("Good day, darling")

        if type(self).__name__ == "Dragon" :
            print("Raaawr")


class Dog(Animal):

    def talk(self):
        super().talk()

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):

    def talk(self):
        super().talk()

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        Animal.__init__(self, name, hunger=0)
        self._stink_count = stink_count

    def talk(self):
        super().talk()

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):

    def talk(self):
        super().talk()

    def sing(self):
        print("Im not your toy")

class Dragon(Animal):

    def __init__(self, name, hunger=0, color = "Green"):
        Animal.__init__(self, name, hunger=0)
        self._color = color

    def talk(self):
        super().talk()

    def breath_fire(self):
        print("$@%@#%#@$%#")



def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst = []
    zoo_lst.extend((dog, cat, skunk, unicorn, dragon))
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)
    zoo_lst.extend((dog2, cat2, skunk2, unicorn2, dragon2))
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal._name)
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()

            if isinstance(animal, Cat):
                animal.chase_laser()

            if isinstance(animal, Skunk):
                animal.stink()

            if isinstance(animal, Unicorn):
                animal.sing()

            if isinstance(animal, Dragon):
                animal.breath_fire()

        while animal.is_hungry():
            animal.feed()
    print(Animal.zoo_name)


main()