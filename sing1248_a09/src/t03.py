"""
-------------------------------------------------------
[Assignment 9, Task 3]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
from functions import file_statistics
file_handle = open("addresses.txt", "r", encoding="utf-8")

a, b, c, d, e = file_statistics(file_handle)
print(a, b, c, d, e)
file_handle.close()
