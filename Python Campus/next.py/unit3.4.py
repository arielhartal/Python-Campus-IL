import string

class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, username, illegal_char, illegal_index):
        self._username = username
        self._illegal_char = illegal_char
        self._illegal_index = illegal_index


    def __str__(self):
        return   "The username contains an illegal character " + str(self._illegal_char) + " at index " + str(self._illegal_index)


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
        return "Your password is missing a required character."

class PasswordMissingDigit(PasswordMissingCharacter):

    def __init__(self, password, digit_miss):
        PasswordMissingCharacter.__init__(self, password)
        self._digit_miss = digit_miss

    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingUpper(PasswordMissingCharacter):

    def __init__(self, password, upper_miss):
        PasswordMissingCharacter.__init__(self, password)
        self._upper_miss = upper_miss

    def __str__(self):
        return super().__str__() + " (Upper)"

class PasswordMissingLower(PasswordMissingCharacter):

    def __init__(self, password, lower_miss):
        PasswordMissingCharacter.__init__(self, password)
        self._lower_miss = lower_miss

    def __str__(self):
        return super().__str__() + " (Lower)"

class PasswordMissingSpecial(PasswordMissingCharacter):

    def __init__(self, password, special_miss):
        PasswordMissingCharacter.__init__(self, password)
        self._special_miss = special_miss

    def __str__(self):
        return super().__str__() + " (Special)"


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
    illegal_index = 0
    illegal_char = ""
    counter = -1
    for i in username:
        counter += 1
        if i in illegal_chars:
            illegal_index = counter
            illegal_char = i
            return illegal_char,illegal_index, True

    return illegal_char, illegal_index, False

def missing_char_in_pass(password):
    special_chars = string.punctuation
    upper_miss = True
    lower_miss = True
    digit_miss = True
    special_miss = True
    for char in password:
        if char.isdigit():
            digit_miss = False
        if char.isupper():
            upper_miss = False
        if char.islower():
            lower_miss = False
        if char in special_chars:
            special_miss = False
    for i in special_chars:
        if i in password and any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password):
            return False, lower_miss, upper_miss, digit_miss, special_miss
    return True, lower_miss, upper_miss, digit_miss, special_miss



def check_input(username, password):
        char, index, bol_user = illegal_char_in_user(username)
        bol_pass, lower_miss, upper_miss, digit_miss, special_miss = missing_char_in_pass(password)

        if bol_user == False and len(username) >= 3 and len(username) <= 16 and len(password) >= 8 and len(password) <= 40 and bol_pass == False :
           print ("OK")

        elif bol_user:
            raise UsernameContainsIllegalCharacter(username, char,index)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)

        elif bol_pass:
            if digit_miss:
                raise  PasswordMissingDigit(password, digit_miss)
            if upper_miss:
                raise PasswordMissingUpper(password, upper_miss)
            if lower_miss:
                raise PasswordMissingLower(password, lower_miss)
            if special_miss:
                raise PasswordMissingSpecial(password, special_miss)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)


def main():
    username = input("Enter your username:")
    password = input("Enter your password:")
    check_input(username, password)

main()
