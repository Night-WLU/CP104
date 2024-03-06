"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
num_flyer = int(input("Number of flyers: "))
num_delivery = int(input("Number of delivery people: "))

flyer_per_delivery = num_flyer // num_delivery
flyer_leftover = num_flyer % num_delivery
print(f'''Flyers per delivery person: {flyer_per_delivery}
Flyers left over: {flyer_leftover}''')
