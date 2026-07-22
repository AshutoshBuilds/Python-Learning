"""
Lesson 01: Introduction to Python
Learning goals: Understand what Python is, run your first program, use print() and comments,
                and see a real GST-style calculation.
Why commerce cares: Accountants, analysts, and entrepreneurs use Python to automate invoices,
                    GST returns, bank reconciliations, and sales reports — saving hours of Excel work.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# Python is a programming language — a way to give step-by-step instructions to a computer.
#
# Think of it like a recipe for a shop:
#   1. Take the selling price
#   2. Calculate 18% GST
#   3. Print the total on the invoice
#
# Python is popular in commerce because:
#   - It reads almost like English (easy for beginners)
#   - It handles numbers, text, and spreadsheets well
#   - Banks, startups, and CA firms use it for automation
#
# HOW TO RUN THIS FILE:
#   Open a terminal in this folder and type:  python 01_introduction.py
#   Or click "Run" in your code editor.
#
# print() — displays text or numbers on the screen (like printing a receipt).
# Comments — lines starting with # are ignored by Python; they explain code for humans.

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("WELCOME TO PYTHON FOR COMMERCE STUDENTS")
print("=" * 50)

# Demo 1: A simple shop banner (text output)
shop_name = "Sharma General Store"
city = "Pune"
print(f"\nShop: {shop_name}, {city}")
print("Thank you for visiting!")

# Demo 2: GST-style calculation (the kind you see on every invoice in India)
# In India, GST (Goods and Services Tax) is added on top of the base price.
# Common rate for many goods: 18%

print("\n--- GST Invoice Preview ---")

item_name = "Office Chair"
base_price = 5000.00          # price before tax (taxable value)
gst_rate_percent = 18         # 18% GST

# GST amount = base price × (rate / 100)
gst_amount = base_price * (gst_rate_percent / 100)

# Total = base + GST (what customer pays)
total_payable = base_price + gst_amount

print(f"Item        : {item_name}")
print(f"Base Price  : Rs. {base_price:,.2f}")
print(f"GST @ {gst_rate_percent}%  : Rs. {gst_amount:,.2f}")
print(f"Total       : Rs. {total_payable:,.2f}")
print("-" * 30)

# Demo 3: Quick profit check (selling price vs cost price)
cost_price = 3500.00
selling_price = 5000.00
profit = selling_price - cost_price

print("\n--- Profit Check ---")
print(f"Cost Price    : Rs. {cost_price:,.2f}")
print(f"Selling Price : Rs. {selling_price:,.2f}")
print(f"Gross Profit  : Rs. {profit:,.2f}")

# Demo 4: Bank balance snapshot (numbers in print)
opening_balance = 25000.00
deposit = 15000.00
withdrawal = 8000.00
closing_balance = opening_balance + deposit - withdrawal

print("\n--- Bank Passbook Snapshot ---")
print(f"Opening Balance : Rs. {opening_balance:,.2f}")
print(f"Deposit (+)     : Rs. {deposit:,.2f}")
print(f"Withdrawal (-)  : Rs. {withdrawal:,.2f}")
print(f"Closing Balance : Rs. {closing_balance:,.2f}")

print("\n[Lesson 01 complete — you ran your first commerce Python program!]")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Print your own shop name and city on separate lines.
# Exercise 2: A notebook costs Rs. 120. GST is 12%. Calculate and print GST and total.
# Exercise 3: Cost price Rs. 80, selling price Rs. 150. Print the profit.

# --- Student code area (Exercise 1) ---
# print("My Shop Name")
# print("My City")

# --- Student code area (Exercise 2) ---
# notebook_price = 120
# gst_rate = 12
# gst = notebook_price * (gst_rate / 100)
# total = notebook_price + gst
# print(f"GST: Rs. {gst}")
# print(f"Total: Rs. {total}")

# --- Student code area (Exercise 3) ---
# cost = 80
# selling = 150
# profit = selling - cost
# print(f"Profit: Rs. {profit}")

# --- Solutions (uncomment to verify) ---
# print("\n--- Exercise Solutions ---")
# print("Gupta Traders")
# print("Mumbai")
# nb_price, nb_gst_rate = 120, 12
# nb_gst = nb_price * (nb_gst_rate / 100)
# print(f"Notebook GST: Rs. {nb_gst}, Total: Rs. {nb_price + nb_gst}")
# print(f"Notebook profit: Rs. {150 - 80}")

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# A customer buys 3 items:
#   Pen     — Rs. 25 each (GST 12%)
#   Register — Rs. 180 each (GST 12%)
#   Stapler  — Rs. 350 each (GST 18%)
# Quantities: 10 pens, 2 registers, 1 stapler.
# Print a simple bill showing each line total (with GST) and the grand total.
#
# Hint: line_total = qty * unit_price * (1 + gst_rate/100)

print("\n--- MINI CHALLENGE (solution shown) ---")
pen_qty, pen_price, pen_gst = 10, 25, 12
reg_qty, reg_price, reg_gst = 2, 180, 12
stap_qty, stap_price, stap_gst = 1, 350, 18

pen_total = pen_qty * pen_price * (1 + pen_gst / 100)
reg_total = reg_qty * reg_price * (1 + reg_gst / 100)
stap_total = stap_qty * stap_price * (1 + stap_gst / 100)
grand_total = pen_total + reg_total + stap_total

print(f"Pens (10 x Rs.25 + {pen_gst}% GST)      : Rs. {pen_total:,.2f}")
print(f"Registers (2 x Rs.180 + {reg_gst}% GST) : Rs. {reg_total:,.2f}")
print(f"Stapler (1 x Rs.350 + {stap_gst}% GST)  : Rs. {stap_total:,.2f}")
print(f"GRAND TOTAL                              : Rs. {grand_total:,.2f}")
