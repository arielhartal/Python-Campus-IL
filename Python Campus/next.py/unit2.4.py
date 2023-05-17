class BigThing:

    def __init__(self, instance):
        self._instance = instance


    def size(self):
        if isinstance(self._instance, int):
            return self._instance
        if isinstance(self._instance, str or dic or list):
            return len(self._instance)

class BigCat(BigThing):

    def __init__(self, instance, weight):
        BigThing.__init__(self, instance)
        self._weight = weight

    def size(self):
        if self._weight > 15 and self._weight < 20 :
            return "Fat"
        elif self._weight > 20 :
            return "Very Fat"
        else:
            return "OK"




def main():
    cutie = BigCat("mitzy", 16)
    print(cutie.size())

main()