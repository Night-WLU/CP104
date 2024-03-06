"""
-------------------------------------------------------
[Lab 2, Task 15]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
MILK = 0.667
BUTTER = 1.333
FLOUR = 0.0833
SALT = 0.333

servings_num = int(input("Enter servings of Mac & Cheese: "))

milk = MILK*servings_num
butter = BUTTER*servings_num
flour = FLOUR*servings_num
salt = SALT*servings_num

print(servings_num, "servings of Mac & Cheese requires:")
print(f"Milk (Cups): {milk:.2f}")
print(f"Butter(Tablespoons): {butter:.2f}")
print(f"Flour(Cups): {flour:.2f}")
print(f"Salt(Teaspoons): {salt:.2f}")
