"""
-------------------------------------------------------
[Lab 8, Task 6]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
from functions import list_stats
small, large, tot, avg = list_stats(
    [94, 96, -22, -79, -28, -26, -50, 71, 24, -32])
print(f"{small:.2f} {large:.2f} {tot:.2f} {avg:.2f}")
