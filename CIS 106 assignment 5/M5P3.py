# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:28:36 2026

@author: shama
"""

books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: "))

order_total = books * cost_per_book

if order_total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00

print(f"Order Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping:.2f}")