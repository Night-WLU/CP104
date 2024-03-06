"""
-------------------------------------------------------
[Lab 10, Task 1]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import customer_record
fh = open("customers.txt", "r", encoding="utf-8")
n = int(input("Enter a record number: "))
res = customer_record(fh, n)
print(res)
