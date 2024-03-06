"""
-------------------------------------------------------
[Functions for Assignment 6]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""


def total_wins():
    """
    -------------------------------------------------------
    counts how many times the input "gold" and "purple" 
    has been provided and exits when enter or return is pressed
    Use: wins = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        wins_purple, wins_gold - two numbers(int) representing num of wins for each team 
    ------------------------------------------------------
    """
    wins_gold = 0
    wins_purple = 0
    entry = "START"
    while entry != "":
        entry = input("Enter the winning team: ")
        if(entry == "purple"):
            wins_purple += 1
        elif(entry == "gold"):
            wins_gold += 1
    return wins_purple, wins_gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    counter = 0
    factor = 2
    while counter < number-1:
        if(number % factor) == 0:
            if(number == factor):
                prime = True
            else:
                prime = False
                break
        factor += 1
        counter += 1
    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_interest_rate = interest_rate/100/12
    remaining_balance = principal_amount
    month = 1
    print("Month Interest   Payment   Balance")
    while remaining_balance > 0:
        monthly_interest = remaining_balance * monthly_interest_rate
        remaining_balance = remaining_balance - payment + monthly_interest

        if remaining_balance < 0:
            payment += remaining_balance
            remaining_balance = 0

        print(
            f"{month:>5d}{monthly_interest:>9.2f}{payment:>10.2f}{remaining_balance:>10.2f}")
        month += 1

    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if number > 0:
        while(number > 0):
            digits += 1
            number = number // 10
    elif number == -1:
        digits += 1
    else:
        while(number < -1):
            digits += 1
            number = number // 10
    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    counter = 0
    factor = 1
    while counter < number-1:
        if(number % factor) == 0:
            total += factor
        factor += 1
        counter += 1
    return total
