"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""
TAX_RATE = 0.185

tot_sales = float(input("Enter the total sales: "))

tax = tot_sales * TAX_RATE

print(f"""
Projected Tax Report
--------------------------
Total sales:   $ {tot_sales:,.2f}
Annual tax:    % 18.50
--------------------------
Tax:           $  {tax:,.2f}""")
