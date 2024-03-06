"""
-------------------------------------------------------
[Lab 10, Task 6]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import number_stats
fh = open("numbers.txt", "r", encoding="utf-8")
s, l, t, a = number_stats(fh)
print(f"{s}, {l}, {t}, {a}")
