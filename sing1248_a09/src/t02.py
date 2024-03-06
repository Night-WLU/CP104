"""
-------------------------------------------------------
[Assignment 9, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
from functions import read_integers
file_handle = open("numbers.txt", "r", encoding="utf-8")
num_list = read_integers(file_handle)
print(num_list)
file_handle.close()
