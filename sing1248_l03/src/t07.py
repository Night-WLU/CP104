"""
-------------------------------------------------------
[Lab 3, Task 7]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""
breakfast = float(input("Enter cost for breakfast: "))
lunch = float(input("Enter cost for lunch: "))
supper = float(input("Enter cost for supper: "))
total = breakfast + lunch + supper
print(f"""
Meal         Cost
Breakfast    ${breakfast:6.2f}
Lunch        ${lunch:6.2f}
Supper       ${supper:6.2f}
Total        ${total:6.2f}""")
