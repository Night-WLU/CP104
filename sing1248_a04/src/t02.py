"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
from functions import pollution_ranking
air_quality_index = int(input("Enter Air Quality Index: "))
pollution = pollution_ranking(air_quality_index)
print(f"Pollution: {pollution}")
