
from file_1 import GreetingCard

class BirthdayCard(GreetingCard):


    def __init__(self, recipient="Dana Ev", sender="Eyal Ch", sender_age=0):
        GreetingCard.__init__(self, recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        return "Happy birthday " + str(self._sender_age)