"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""

from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 0
    number = randint(1, high)
    guess = 0
    while guess != number:
        guess = int(input("Guess: "))
        if(guess < number):
            print("Too low")
        elif(guess > number):
            print("Too high")
        count = count+1
    print("Congratulations - good guess")
    print(f"You made {count} guesses")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    exponent = 0
    power = 2 ** exponent
    while power < target:
        exponent = exponent + 1
        power = 2 ** exponent
    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    final = 1
    counter = 1
    total = 0
    while final < target:
        final = total + counter**2
        total = final
        counter = counter + 1
    return final


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    entry = float(input("Enter an expense (0 to quit): "))
    temp_cost = entry
    while entry != 0:
        entry = float(input("Enter another expense (0 to quit):"))
        available = available - entry
        cost = entry + temp_cost

    if available < 0:
        status = "Deficit"
    elif available == 0:
        status = "Balanced"
    else:
        status = "Surplus"
    return cost, available, status


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    OVERTIME = 1.5
    TAX = 0.03625
    OVERTIME_THRESHOLD = 40
    extra_hours = 0
    pay = 0
    total = 0
    counter = 0
    identity = 1
    extra_pay = 0
    while identity != 0:
        identity = int(input("Employee ID: "))
        if identity == 0:
            break
        rate = float(input("Hourly wage rate: "))
        num_hours = float(input("Hours worked: "))
        if num_hours > OVERTIME_THRESHOLD:
            extra_hours = num_hours - OVERTIME_THRESHOLD
            num_hours = OVERTIME_THRESHOLD
        extra_pay = extra_hours * rate * OVERTIME
        pay = (rate * num_hours)
        pay = pay + extra_pay
        tax = pay * TAX
        pay = pay - tax
        print(f"Net payment for employee {identity}: {pay:.2f}")
        total = total + pay
        counter = counter + 1
        extra_pay = 0
        extra_hours = 0
    average = total / counter
    average = float("{:.2f}".format(average))
    total = float("{:.2f}".format(total))
    return total, average
