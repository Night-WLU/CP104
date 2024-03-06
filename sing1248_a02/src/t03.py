"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
unformatted = int(input("Enter a date in the format YYYYMMDD: "))
year = unformatted // 10000
month = unformatted % 10000
month = month // 100
day = unformatted % 100
print(f"""The reformatted date: {year}/{month:02d}/{day:02d}""")
