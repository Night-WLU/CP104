"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
from functions import footage_to_acres

acres = float(input("input: "))
acres = footage_to_acres(acres)
print(f"output: {acres}")
