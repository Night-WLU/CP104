"""
-------------------------------------------------------
[Lab 9, Task 3]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
from functions import parse_code
code = input("Enter Code: ")
a, b, c = parse_code(code)
print(f"parse_code('{code}') -> ('{a}', '{b}', '{c}')")
