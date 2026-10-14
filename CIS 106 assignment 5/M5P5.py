# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:33:59 2026

@author: shama
"""

last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

adjusted_gross_income = gross_income - (dependents * 12000)

if adjusted_gross_income > 50000.00:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_gross_income * tax_rate

if income_tax < 0:
    income_tax = 100.00

print(f"Last Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Dependents: {dependents}")
print(f"Adjusted Gross Income: ${adjusted_gross_income:.2f}")
print(f"Income Tax: ${income_tax:.2f}")