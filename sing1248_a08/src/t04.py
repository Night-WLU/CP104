"""
-------------------------------------------------------
[Assignment 8, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
from functions import valid_isbn
isbn = input('Enter ISBN: ')
is_valid = valid_isbn(isbn)
print(f"valid_isbn({isbn}) -> {is_valid}")
