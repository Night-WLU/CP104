"""
-------------------------------------------------------
[Assignment 9, Task 1]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
from functions import file_top
file_handle = open("students.txt", "r", encoding="utf-8")
file_top(file_handle, 5)
file_handle.close()
