"""
-------------------------------------------------------
[Assignment 7, Task 1]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
from functions import list_factors
num = int(input("Enter num: "))
factor_list = list_factors(num)
print(f"list_factors({num}) -> {factor_list}")
