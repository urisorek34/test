"""
Author: Uri Sorek
Date: 14/11/2022
Get number input and check validation
"""


class NumberHasLettersException(IOError):
    """
    class for if the input has letters
    """

    def __int__(self):
        pass

    def __str__(self):
        return "the number has letters"


class NumberHasTooManyPointsException(IOError):
    """
    class for if the input has too many decimal points
    """

    def __int__(self):
        pass

    def __str__(self):
        return "the number has letters"


def get_input():
    """
    functions returns the inputted number.
    :return: the input number
    """

    try:
        num_str = input("Get a number: ")
        num_lst = num_str.split(".")
        i = 0
        # dont check if negative
        while num_str[i] == '-':
            i += 1
        num_str = num_str[i:]
        for decimal_side in num_lst:
            # check for decimal points
            if not decimal_side.isdigit():
                print(NumberHasLettersException)
                raise NumberHasLettersException
            if len(num_lst) > 2:
                # if number has more than one decimal point
                print(NumberHasTooManyPointsException)
                raise NumberHasTooManyPointsException

        return float(num_str) + 1
    except EOFError as e:
        # if end of file exception
        print(e)


if __name__ == "__main__":
    print(get_input())
