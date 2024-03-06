"""
-------------------------------------------------------
[Assignment 7, Functions]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(number):
    """
    -------------------------------------------------------
    Returns the factor for an integer more than zero
    Use: factor_list = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - number to find the factors of (int)
    Returns:
        factor_list - list with the possible factors excluding the number itself (list of ints)
    ------------------------------------------------------
    """
    factor_list = []
    for i in range(1, number, 1):
        if number % i == 0:
            factor_list.append(i)
    return factor_list


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    entry = int(input('Enter a positive number: '))
    while entry != 0:
        if entry > 0:
            number_list.append(entry)
        entry = int(input('Enter a positive number: '))
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    length = len(numbers)
    index_list = []
    for i in range(length):
        if numbers[i] == target_number:
            index_list.append(i)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    removal = []

    for i in minuend:
        if i in subtrahend:
            removal.append(i)

    for i in removal:
        minuend.remove(i)

    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    length = len(numbers)
    for i in range(0, length-1, 1):
        if numbers[i] < numbers[i+1]:
            in_order = True
            index = -1
        else:
            in_order = False
            index = i+1
            break
    return in_order, index
