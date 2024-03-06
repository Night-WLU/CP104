"""
-------------------------------------------------------
[Functions For Lab 8]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    names = ["one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    name = names[n-1]
    return name


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    length = len(values)
    values.sort()
    smallest = values[0]
    values.reverse()
    values1 = values
    largest = values[0]
    total = 0
    for _ in range(0, length, 1):
        total += values1.pop()
    avg = total / length
    return smallest, largest, total, avg


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = []
    length = len(values)
    for i in range(length):
        if values[i] == value:
            indexes.append(i)
    return indexes


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    length = len(source1)
    for i in range(length):
        new_val = source1[i] + source2[i]
        target.append(new_val)
    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    length1 = len(source1)
    length2 = len(source2)
    if length1 > length2:
        bigger = length1
        smaller = length2
        bigger_list = source1
        smaller_list = source2
    else:
        bigger = length2
        smaller = length1
        bigger_list = source2
        smaller_list = source1
    for i in range(bigger):
        for j in range(smaller):
            if bigger_list[i] == smaller_list[j]:
                if (bigger_list[i] in target) == False:
                    target.append(bigger_list[i])
    target.reverse()
    return target
