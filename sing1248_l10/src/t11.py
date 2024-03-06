"""
-------------------------------------------------------
[Lab 10, Task 11]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import find_longest
fh = open("words.txt", "r", encoding="utf-8")
word = find_longest(fh)
print(word)
