"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:   Sukhman Singh
ID:      
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
num_years = int(input("Number of years: "))
num_compounded_per_year = int(
    input("Number of time interest compounded per year: "))

interest = interest / 100

calculation_in_bracket = 1 + (interest / num_compounded_per_year)
calculation_exponent = num_compounded_per_year * num_years
calculation_bracket_exponent = calculation_in_bracket ** calculation_exponent
balance = principal * calculation_bracket_exponent

print("Balance: $", balance)
