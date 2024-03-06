"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
number = float(input("Enter number: "))
percent = float(input("Enter percent: "))
discount = float(number * (percent/100))

print(f"A {percent} percent discount on {number} is {discount:.1f}")
