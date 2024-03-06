"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""

pos = int(input("Enter a positive digit number: "))
first = pos // 10
second = pos % 10
diff = first - second
print(f"The difference of the digits of {pos} is {diff}")
