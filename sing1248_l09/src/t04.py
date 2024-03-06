"""
-------------------------------------------------------
[Lab 9, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
from functions import validate_code
product_code = input("Enter input: ")
category, digits, qualifiers = validate_code(product_code)
print(f"validate_code({product_code}) -> ('{category}','{digits}','{qualifiers}')")
