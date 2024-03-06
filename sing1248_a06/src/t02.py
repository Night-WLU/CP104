"""
-------------------------------------------------------
[Assignment 6, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
from functions import detect_prime
num = int(input("Enter num: "))
detect = detect_prime(num)
print(f"detect_prime({num}) -> {detect}")
