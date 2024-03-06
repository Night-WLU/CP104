"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
from functions import multiply_fractions

num1 = int(input("Enter numerator for fraction 1: "))
den1 = int(input("Enter denum for fraction 1: "))
num2 = int(input("Enter numerator for fraction 2: "))
den2 = int(input("Enter denum for fraction 2: "))

product = multiply_fractions(num1, den1, num2, den2)

print(product)
