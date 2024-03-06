"""
-------------------------------------------------------
[Lab 2, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""

FREEZING = 32
degrees_f = int(input("Temperature (F): "))
degrees_c = (degrees_f - FREEZING) * (5/9)
print("Temperature (C): ", degrees_c)
