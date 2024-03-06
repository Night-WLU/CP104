"""
-------------------------------------------------------
[Lab 2, Task 6]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""

mortgage_principal = float(input("Mortgage principal ($): "))
number_of_years = int(input("Number of years: "))
yearly_interest_rate = float(input("Yearly interest rate: "))

monthly_interest = (yearly_interest_rate/100)/12
num_monthly_payments = number_of_years * 12
calculation_step1 = (1 + monthly_interest)**num_monthly_payments
calculation_step2 = monthly_interest * calculation_step1
calculation_step3 = calculation_step1 - 1
calculation_step4 = calculation_step2 / calculation_step3

monthly_payments = mortgage_principal * calculation_step4

print("The monthly payments are: ", monthly_payments)
