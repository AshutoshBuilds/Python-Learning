"""
Lesson 05: Input and Output
Learning goals: Formatted print output, optional input() behind USE_INPUT flag,
                type casting (int, float, str), and building a demo invoice from variables.
Why commerce cares: POS systems, billing apps, and loan calculators all read user input
                    and display polished receipts and statements.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# OUTPUT — print() with formatting:
#   print(f"Amount: {x:,.2f}")     comma separators, 2 decimals
#   print(f"{name:<20}")           left-align in 20 chars
#   print(f"{qty:>5}")             right-align
#   print("-" * 40)                repeat character for lines
#
# INPUT — input("prompt") returns a STRING always.
#   To use as number: amount = float(input("Enter amount: "))
#
# TYPE CASTING:
#   int("42")     → 42
#   float("18.5") → 18.5
#   str(1000)     → "1000"
#
# IMPORTANT: This lesson uses DEMO VALUES by default so the file runs without waiting.
# Set USE_INPUT = True only when you want to practice interactive entry.

USE_INPUT = False   # Change to True to enable interactive input blocks below

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("INPUT & OUTPUT — FORMATTED INVOICE")
print("=" * 50)

# --- Demo 1: Rich print formatting ---
print("\n{:<20} {:>10} {:>12}".format("Item", "Qty", "Amount"))
print("-" * 44)
print("{:<20} {:>10} {:>12,.2f}".format("A4 Paper Ream", 5, 1250.00))
print("{:<20} {:>10} {:>12,.2f}".format("Ink Cartridge", 2, 3400.00))
print("-" * 44)
print("{:>32} {:>12,.2f}".format("Subtotal:", 4650.00))

# --- Demo 2: Demo invoice built from variables (default path) ---
seller_name = "BluePeak Stationers"
seller_gstin = "29AABCB1234C1Z9"
buyer_name = "Horizon Coaching Centre"
invoice_no = "BP/2026/0087"
invoice_date = "09-Jul-2026"

items = [
    ("Whiteboard Marker", 24, 35.00),
    ("Register 200pg", 10, 85.00),
    ("Geometry Box", 15, 120.00),
]

gst_rate = 12.0

print("\n" + "=" * 55)
print(f"{'TAX INVOICE':^55}")
print("=" * 55)
print(f"Seller : {seller_name}")
print(f"GSTIN  : {seller_gstin}")
print(f"Buyer  : {buyer_name}")
print(f"Inv No : {invoice_no}    Date: {invoice_date}")
print("-" * 55)
print(f"{'Description':<28} {'Qty':>6} {'Rate':>10} {'Amount':>10}")
print("-" * 55)

subtotal = 0.0
for desc, qty, rate in items:
    amount = qty * rate
    subtotal += amount
    print(f"{desc:<28} {qty:>6} {rate:>10,.2f} {amount:>10,.2f}")

gst_amount = round(subtotal * (gst_rate / 100), 2)
grand_total = subtotal + gst_amount

print("-" * 55)
print(f"{'Taxable Value':<44} {subtotal:>10,.2f}")
print(f"{f'CGST @ {gst_rate/2}%':<44} {gst_amount/2:>10,.2f}")
print(f"{f'SGST @ {gst_rate/2}%':<44} {gst_amount/2:>10,.2f}")
print(f"{'GRAND TOTAL':<44} {grand_total:>10,.2f}")
print("=" * 55)

# --- Demo 3: Optional interactive input (NOT executed by default) ---
if USE_INPUT:
    print("\n--- Interactive Mode ---")
    customer = input("Customer name: ")
    units = int(input("Quantity: "))
    price = float(input("Unit price (Rs.): "))
    line_total = units * price
    print(f"Line total for {customer}: Rs. {line_total:,.2f}")
else:
    # Demo values simulating what input() would capture
    customer = "Demo Customer Pvt Ltd"
    units = 8
    price = 450.50
    line_total = units * price
    print(f"\n[Demo mode] Line total for {customer}: Rs. {line_total:,.2f}")
    print("(Set USE_INPUT = True at top of file to type your own values)")

# --- Demo 4: Casting strings to numbers (common in CSV/import) ---
csv_price = "1299.99"
csv_qty = "3"
computed = float(csv_price) * int(csv_qty)
print(f"\nFrom CSV strings '{csv_price}' x '{csv_qty}' = Rs. {computed:,.2f}")

# --- Demo 5: Bank statement line output ---
transactions = [
    ("09-Jul", "NEFT Credit - Client Payment", 25000.00),
    ("08-Jul", "UPI - Office Supplies", -1850.00),
    ("07-Jul", "Cash Deposit", 10000.00),
]
balance = 125000.00
print("\n--- Mini Bank Statement ---")
print(f"{'Date':<8} {'Description':<30} {'Amount':>12} {'Balance':>12}")
print("-" * 64)
for date, desc, amt in reversed(transactions):
    balance += amt if date == "09-Jul" else 0  # simplified running balance demo
    sign = "+" if amt >= 0 else ""
    print(f"{date:<8} {desc:<30} {sign}{amt:>11,.2f} {balance:>12,.2f}")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Print a 3-column table header: SKU, Product, Price (aligned).
# Exercise 2: With USE_INPUT=False, use demo cost=500, qty=4, print total.
# Exercise 3: Cast "18" and "2500.50" to int and float; print their product.

# --- Student code area ---
# print(f"{'SKU':<10} {'Product':<20} {'Price':>10}")

# --- Solutions ---
# cost, qty = 500, 4
# print(cost * qty)
# print(int("18") * float("2500.50"))  # careful: int*float works

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Print a complete payment receipt using only variables and formatted print.
# Include: receipt no, payer, mode (UPI/Cash), amount in figures.

print("\n--- MINI CHALLENGE: Payment Receipt ---")
receipt_no = "RCT-2026-0441"
payer = "Mehta Industries"
payment_mode = "UPI"
amount_received = 67500.00
payment_date = "09-Jul-2026"

print("+" + "-" * 48 + "+")
print(f"|{'PAYMENT RECEIPT':^48}|")
print("+" + "-" * 48 + "+")
print(f"| Receipt No : {receipt_no:<32}|")
print(f"| Date       : {payment_date:<32}|")
print(f"| Received from: {payer:<30}|")
print(f"| Mode       : {payment_mode:<32}|")
print(f"| Amount     : Rs. {amount_received:>24,.2f} |")
print("+" + "-" * 48 + "+")
print(f"|{'Thank you for your payment!':^48}|")
print("+" + "-" * 48 + "+")
