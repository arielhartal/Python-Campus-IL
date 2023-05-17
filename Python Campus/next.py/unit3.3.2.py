class UnderAge(Exception):

    def __init__(self,name, age):
        self._age = age
        self._name = name

    def __str__(self):
        return  self._name + " your age: (" + str(self._age) + ") is not 18 or above. " + "Could join in " + str(18-self._age) + " years."

    def get_age(self):
        return self._age

def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(name, age)
    else:
        print("You should send an invite to " + name)
        return ""

print(send_invitation("Toni", 20))