class IDIterator:
    """
        A class used to represent an Id number in iterator form, has to be between 0 and 999999999
       if it reaches 999999999 it raises a StopIteration exception
    """
    def __init__(self, id):
        if int(id) > 0 and int(id) < 999999999:
            self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while check_id_valid(self._id) == False:
            self._id += 1
        return self._id

        if self._id == 999999999:
            """ :raise: StopIteration: raises an Exception """
            raise StopIteration


class InvalidInput(Exception):
    """
        A class used to represent an exception of getting an invalid input from the user
    """

    def __str__(self):
        return "Your input is invalid"


class NotNumeric(InvalidInput):
    """
           A class used to represent an exception of getting an input that isnt numeric (isnt valid) from the user
    """

    def __str__(self):
        return super().__str__() + ", it consists an invalid character, try again"

class TooLong(InvalidInput):
    """
           A class used to represent an exception of getting an input that consists more than 9 characters
    """

    def __str__(self):
        return super().__str__() + ", its too long, try again"

class TooShort(InvalidInput):
    """
           A class used to represent an exception of getting an input that consists less than 9 characters
    """

    def __str__(self):
        return super().__str__() + ", its too short, try again"





def multiply_by_place(id_number):
    """ Multiply the digit according to the place, if the digit is in even place
        it multiplies by 2 and if its in odd place it multiplies by 1
        :param id_number: id_number value
        :type id_number: int
        :return: New id number after multiplying digits according to place
        :rtype: list
    """
    place = 1
    multiplied_id_number = []
    id_number = str(id_number)
    ','.join(id_number)
    for num in id_number:
        if place % 2 == 0:
            num = int(num)*2
            multiplied_id_number.append(num)
        else:
            num = int(num)
            multiplied_id_number.append(num)
        place += 1
    return multiplied_id_number



def check_if_bigger_than_nine(multiplied_id_number):
    """ Checking the digits of the id number, if digit is bigger than nine change it to the sum of
        both digits, if not it stays the same
        :param multiplied_id_number: multiplied_id_number value
        :type multiplied_id_number: list
        :return: New id number after checking which digits are bigger than 9 and summing their digits if they are
        :rtype: list
    """
    bigger_than_nine_id_number = []
    for num in multiplied_id_number:
        if int(num) > 9:
            sum = 0
            for digit in str(num):
                sum += int(digit)
            bigger_than_nine_id_number.append(sum)
        else:
            bigger_than_nine_id_number.append(num)
    return bigger_than_nine_id_number



def summary(bigger_than_nine_id_number):
    """ Summing the digits of the id number after multiplying according to place
        and checking which digits are bigger than 9
        :param bigger_than_nine_id_number: bigger_than_nine_id_number value
        :type bigger_than_nine_id_number: list
        :return: The sum of the id number after the first two steps
        :rtype: int
    """
    return (sum(num for num in bigger_than_nine_id_number))



def check_id_valid(id_number):
    """ Checking if the id is number, after summing the id number after the first 2 steps it checks
        if it can divided by 10, if it is its valid if not its not valid
        :param id_number: id_number value
        :type id_number: int
        :return: True if its valid (can be divided by 10) false if not
        :rtype: boolean
    """
    multiplied_id_number = multiply_by_place(id_number)
    bigger_than_nine_id_number = check_if_bigger_than_nine(multiplied_id_number)
    sum_id_number = summary(bigger_than_nine_id_number)
    if sum_id_number % 10 == 0:
        return True
    else:
        return False



def id_generator(id_number):
    """ Returns (Yields) the next valid id number after the one that has been entered and while its in the
        valid range (0 until 999999999)
        :param id_number: id_number value
        :type id_number: int
        :return (yield): The next valid id number after the one that has been entered
        :rtype: int
    """
    while id_number < 999999999 and id_number > 0:
        while check_id_valid(id_number) == False:
            id_number += 1
        yield id_number
        id_number += 1



def delete_zeros(id_number):
    """ Returns the id number after deleting the zeros from the left side of the id number
        :param id_number: id_number value
        :type id_number: str
        :return: The id number without the zeros on the left side of it
        :rtype: string
    """
    id_number = id_number.lstrip("0")
    return id_number


def main():
    """ Asks for an id number from the user and checks if its valid,
     if not it raises the suitable exception, if the id number is valid it asks the user
     to enter how he wants the function to run, via generator or via iterator
    """
    id_number = input("Enter your id number:")
    if id_number.isnumeric() == False:
        raise NotNumeric
    id_number = delete_zeros(id_number)
    if len(id_number) < 9:
        raise TooShort
    if len(id_number) > 9:
        raise TooLong
    else:
        gen_or_it = input("Generator or Iterator? (gen/it)?")
        if gen_or_it != "gen" and gen_or_it != "it":
           raise InvalidInput
        if gen_or_it == "gen":
            gen_id = (id_generator(int(id_number)))
            for i in range(10):
                print(next(gen_id))
        if gen_or_it == "it":
            iter_id = IDIterator(int(id_number))
            for i in range(10):
                print(iter_id.__next__())


main()