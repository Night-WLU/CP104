"""
-------------------------------------------------------
[Assignment 4, Task 3]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
from functions import largest_average
val1 = float(input("Enter Value 1: "))
val2 = float(input("Enter Value 2: "))
val3 = float(input("Enter Value 3: "))
average = largest_average(val1, val2, val3)
print(f"Average: {average:,.2f}")
