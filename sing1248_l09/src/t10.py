"""
-------------------------------------------------------
[Lab 9, Task 10]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
from functions import text_analyze
txt = input("Enter input: ")
a, b, c, d = text_analyze(txt)
print(f"text_analyse({txt}) -> ({a}, {b}, {c}, {d})")
