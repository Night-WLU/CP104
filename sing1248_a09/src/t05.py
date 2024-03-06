"""
-------------------------------------------------------
[Assignment 9, Task 5]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
from functions import student_stats
fh_read = open("students.txt", "r", encoding="utf-8")
low, high, avg = student_stats(fh_read)
fh_read.close()
print(f"{low}  {high}  {avg}")
