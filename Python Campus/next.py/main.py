from file_1 import GreetingCard
from file_2 import BirthdayCard

def main():
    g = GreetingCard()
    b = BirthdayCard()
    print(GreetingCard.greeting_msg(g))
    print(BirthdayCard.greeting_msg(b))

main()