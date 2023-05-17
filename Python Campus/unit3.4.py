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
        self._username = password

    def __str__(self):
        return "Your password: %s is missing a required character." % self._password


class PasswordTooShort(Exception):

    def __init__(self, password):
        self._username = password

    def __str__(self):
        return "Your password: %s is too short." % self._password

class PasswordTooLong(Exception):

    def __init__(self, password):
        self._username = password

    def __str__(self):
        return "Your password: %s is too long." % self._password


def illegal_char_in_user(username):
    illegal_chars = string.punctuation.remove("_")
    for i in username:
        if i in illegal_chars:
            return True:


def check_input(username, password):
        if illegal_char_in_user(username) == False and len(username) > 3 and len(username) < 16:
            return "OK"
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)

print(check_input)