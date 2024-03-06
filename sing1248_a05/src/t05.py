"""
-------------------------------------------------------
[Assignment 5, Task 5]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
from functions import range_addition
start = int(input("Start: "))
increment = int(input("Incr: "))
count = int(input("Count: "))
total = range_addition(start, increment, count)
print(f"range_addition({start}, {increment}, {count}) -> {total}")
