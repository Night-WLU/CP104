"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""

from functions import lawn_mow_time

width = float(input("Enter Width: "))
length = float(input("Enter Length: "))
speed = float(input("Enter Speed: "))
time = lawn_mow_time(width, length, speed)
print(f"Time:{time} seconds")
