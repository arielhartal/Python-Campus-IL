class Octopus:

     def __init__(self ,name="Octavio", age=10):
        self.name = name
        self.age = age


     def birthday(self):
        self.age += 1

     def get_age(self):
        return self.age


def main():
    oct1 = Octopus()
    oct2 = Octopus()
    oct1.birthday()
    print(oct1.get_age(), oct2.get_age())


main()
