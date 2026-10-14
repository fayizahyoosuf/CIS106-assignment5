# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:31:06 2026

@author: shama
"""

appliance_name = input("Enter appliance name: ")
cost = float(input("Enter appliance cost: "))

if cost > 1000.00:
    warranty_cost = cost * 0.10
else:
    warranty_cost = cost * 0.05

total_cost = cost + warranty_cost

print(f"Appliance: {appliance_name}")
print(f"Cost: ${cost:.2f}")
print(f"Warranty Cost: ${warranty_cost:.2f}")
print(f"Total: ${total_cost:.2f}")