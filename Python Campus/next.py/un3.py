import string

class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, username):
        self._username = username

    def __str__(self):
        return   "Your Username: %s contains illegal character." % self._username


class UsernameTooShort(Exception):

    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your Username: %s is too short." % self._username


class UsernameTooLong(Exception):

    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your Username: %s is too Long." % self._username



class PasswordMissingCharacter(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password: %s is missing a required character." % str(self._password)


class PasswordTooShort(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password: %s is too short." % str(self._password)

class PasswordTooLong(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password: %s is too long." % str(self._password)


def illegal_char_in_user(username):
    illegal_chars = string.punctuation.replace("_", "")
    for i in username:
        if i in illegal_chars:
            return True
    return False

def missing_char_in_pass(password):
    special_chars = string.punctuation
    for i in special_chars:
        if i in password and any(char.isdigit() and char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password):
            return False
    return True



def check_input(username, password):

        if illegal_char_in_user(username) == False and len(username) > 3 and len(username) < 16 and len(password) > 8 and len(password) <= 40 and missing_char_in_pass(password) == False :
            return "OK"



        elif illegal_char_in_user(username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)

        elif missing_char_in_pass(password):
            raise PasswordMissingCharacter(password)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)



try:

    print(check_input("A8_1", "123aA!555DF"))

except UsernameTooShort as e:
    print(e)
except PasswordTooShort as e1:
    print(e1)
except PasswordTooLong as e2:
    print(e2)
except UsernameTooLong as e3:
    print(e3)
except UsernameContainsIllegalCharacter as e4:
    print(e4)
except PasswordMissingCharacter as e5:
    print(e5)


    


