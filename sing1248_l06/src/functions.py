"""
-------------------------------------------------------
[Functions for Lab 6]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-27"
-------------------------------------------------------
"""


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    for i in range(start, finish, increment):
        start = start + increment + i
    return start


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    space = " "
    for i in range(0, width, 1):
        if(i < 1):
            print(f"{char}")
        elif(i < 2):
            print(f"{char}{char*i:.2s}")
        elif(i == width-1):
            print(f"{char}{char*i}")
        else:
            print(f"{char}{space*(i-1)}{char}")
    return None


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    RETIREMENT = 65
    years_worked = RETIREMENT - age
    print(f"Age{'Salary':>15s}")
    for _ in range(years_worked+1):
        print(f"{age}{salary:>16,.2f}")
        age = age + 1
        percentage_increase = (increase/100)
        salary_increase = salary * percentage_increase
        salary = salary + salary_increase
    return None
# Task Incomplete. Figure out width of spacing


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print('''              Cross-Sectional  Moment of  Section
Base  Height  Area             Inertia    Modulus''')
    for base in range(b_min, b_max+b_inc, b_inc):
        for height in range(h_min, h_max+h_inc, h_inc):
            area = base * height
            inertia = base * height ** 3 / 12
            modulus = base * height ** 2 / 6
            print(
                f"{base:>4d}  x{height:>5d}{area:>17.2f}{inertia:>11.2f}{modulus:9.2f}")
    return None


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    MAX_WEEKS = 6
    total_hours = 0
    counter = 1
    for _ in range(0, MAX_WEEKS, 1):
        print(f"Week {counter}")
        for i in range(ia_count):
            hours = float(input(f"Marking hours for IA {i+1}: "))
            total_hours += hours
        counter = counter + 1
    return total_hours
