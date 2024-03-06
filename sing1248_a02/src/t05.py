"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_concrete = float(input("Cost of concrete ($/m^3): "))
cost_bricks = float(input("Cost of bricks ($/m^2): "))

foundation = length * width * height
concrete = foundation * cost_concrete
num_bricks = (2 * (length * wall_height)) + (2 * (width * wall_height))
cost = cost_bricks * num_bricks
tot = cost + concrete

print(f""" 
Concrete needed for foundation (m^3): {foundation:,.2f}
Cost of concrete: ${concrete:,.2f}
Bricks needed for walls (m^2): {num_bricks:,.2f}
Cost of bricks: ${cost:,.2f}
Total cost: ${tot:,.2f}""")
