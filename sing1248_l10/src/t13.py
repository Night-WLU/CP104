"""
-------------------------------------------------------
[Lab 10, Task 13]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import file_copy
fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("word.txt", "w", encoding="utf-8")
file_copy(fh_1, fh_2)
