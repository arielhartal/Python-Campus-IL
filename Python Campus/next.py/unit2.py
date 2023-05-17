

class Octopus:

    count = 0

    def __init__(self ,name="Octavio", age=10):
        self._name = name
        self._age = age
        Octopus.count += 1


    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
         self._name = name

    def get_name(self):
         return self._name




    

def main():
    oct1 = Octopus()
    oct2 = Octopus()
    oct1.birthday()
    oct2.set_name("Yossi")
    print(oct1.get_name(), oct2.get_name())
    oct1.set_name("Toni")
    print(oct1.get_name())
    print(Octopus.count)



main()
