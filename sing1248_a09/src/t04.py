"""
-------------------------------------------------------
[Assignment 9, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
from functions import line_numbering
fh_read = open("wilde.txt", "r", encoding="utf-8")
output = open("wilde_copy.txt", "w", encoding="utf-8")
line_numbering(fh_read, output)
fh_read.close()
output.close()
