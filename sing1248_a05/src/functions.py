"""
-------------------------------------------------------
[Assignment 5, Functions]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number+1, 1):
        product = i * product
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned per minute (float)
        minutes - total number of minutes run (float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(5, minutes+1, 5):
        calories = i * per_min
        print(f"{i:>2}  {calories:.1f}")
    return None


def arrow_up(rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints a arrow of # characters pointing up.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows for the height of the arrow (int)
    Returns:
        None
    ------------------------------------------------------
    """
    char = '#'
    print(f"{char:>{rows}s}")
    for i in range(1, rows, 1):
        print(f"{char:>{rows-i}s}{char:>{i*2}s}")
    return None


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    output = ""
    top = f"{start_num:>7d}"
    for i in range(start_num+1, stop_num+1, 1):
        top += f"{i:>4d}"
    print(top)
    for i in range(start_num, stop_num+1, 1):
        output = f"{i:<2d}|"
        for j in range(start_num, stop_num+1, 1):
            factor = j*i
            output += f"{factor:>4d}"
        print(output)
    return None


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total = total + start + (i*increment)
    return total
