"""
Lesson 10: Dictionaries
Learning goals: Use dicts for invoice lines, ledger accounts, and customer records
                with keys and values.
Why commerce cares: Every ERP, billing app, and accounting system stores data as
                    key-value records — customer name, GSTIN, balance, line items.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# A DICTIONARY maps KEYS to VALUES:  {key: value, key2: value2}
#
# CREATE:
#   customer = {"name": "Mehta Ltd", "gstin": "27AAA...", "credit_limit": 100000}
#
# ACCESS:
#   customer["name"]           direct key
#   customer.get("phone", "N/A")  safe — default if key missing
#
# MODIFY:
#   customer["phone"] = "9876543210"   add or update
#   del customer["temp_field"]
#
# ITERATE:
#   for key in customer:
#   for key, value in customer.items():
#
# NESTED DICTS — invoice with multiple line items as list of dicts (common pattern)

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("DICTIONARIES — INVOICES, LEDGER, CUSTOMERS")
print("=" * 50)

# --- Demo 1: Customer record ---
customer = {
    "id": "CUST-0042",
    "name": "Apex Distributors Pvt Ltd",
    "gstin": "27AABCA1234B1Z9",
    "pan": "AABCA1234B",
    "city": "Pune",
    "credit_limit": 500000.00,
    "outstanding": 187500.00,
    "payment_terms_days": 30,
    "is_active": True,
}

print("\n--- Customer Record ---")
for key, value in customer.items():
    if isinstance(value, float):
        print(f"  {key:<22}: Rs. {value:,.2f}" if "limit" in key or "outstanding" in key
              else f"  {key:<22}: {value}")
    else:
        print(f"  {key:<22}: {value}")

available_credit = customer["credit_limit"] - customer["outstanding"]
print(f"\n  Available credit     : Rs. {available_credit:,.2f}")

# --- Demo 2: Invoice as dictionary with line items ---
invoice = {
    "invoice_no": "INV/2026/0892",
    "date": "09-Jul-2026",
    "seller_gstin": "27AABCB5678C1Z5",
    "buyer": customer["name"],
    "buyer_gstin": customer["gstin"],
    "place_of_supply": "Maharashtra",
    "lines": [
        {"desc": "HP Laptop 15", "hsn": "8471", "qty": 2, "rate": 45000.00, "gst_pct": 18},
        {"desc": "Wireless Mouse", "hsn": "8471", "qty": 2, "rate": 850.00, "gst_pct": 18},
        {"desc": "Laptop Bag", "hsn": "4202", "qty": 2, "rate": 1200.00, "gst_pct": 18},
    ],
}

print("\n--- Tax Invoice ---")
print(f"Invoice : {invoice['invoice_no']}  Date: {invoice['date']}")
print(f"Buyer   : {invoice['buyer']}")
print(f"GSTIN   : {invoice['buyer_gstin']}")
print("-" * 60)
print(f"{'Description':<20} {'HSN':<6} {'Qty':>4} {'Rate':>10} {'Taxable':>12}")
print("-" * 60)

total_taxable = 0.0
total_gst = 0.0

for line in invoice["lines"]:
    taxable = line["qty"] * line["rate"]
    gst_amt = taxable * (line["gst_pct"] / 100)
    total_taxable += taxable
    total_gst += gst_amt
    print(f"{line['desc']:<20} {line['hsn']:<6} {line['qty']:>4} "
          f"{line['rate']:>10,.2f} {taxable:>12,.2f}")

grand_total = total_taxable + total_gst
print("-" * 60)
print(f"{'Taxable Value':<42} {total_taxable:>12,.2f}")
print(f"{'Total GST':<42} {total_gst:>12,.2f}")
print(f"{'GRAND TOTAL':<42} {grand_total:>12,.2f}")

# --- Demo 3: Ledger account (T-account style balances) ---
ledger = {
    "Cash": {"debit": 125000.00, "credit": 45000.00},
    "Sales": {"debit": 0.00, "credit": 380000.00},
    "Purchases": {"debit": 210000.00, "credit": 0.00},
    "GST Payable": {"debit": 15000.00, "credit": 42000.00},
    "Rent Expense": {"debit": 25000.00, "credit": 0.00},
}

print("\n--- Ledger Balances ---")
print(f"{'Account':<18} {'Debit':>14} {'Credit':>14} {'Balance':>14}")
print("-" * 62)

for account, entries in ledger.items():
    balance = entries["debit"] - entries["credit"]
    side = "Dr" if balance >= 0 else "Cr"
    print(f"{account:<18} {entries['debit']:>14,.2f} {entries['credit']:>14,.2f} "
          f"{abs(balance):>12,.2f} {side}")

# --- Demo 4: GST rate lookup table ---
gst_slab_table = {
    "milk_fresh": 0,
    "packaged_food": 5,
    "apparel": 12,
    "electronics": 18,
    "luxury_hotel": 28,
}

product_type = "electronics"
rate = gst_slab_table.get(product_type, 18)
demo_price = 25000
gst_on_item = demo_price * (rate / 100)
print(f"\n--- GST Lookup: {product_type} @ {rate}% on Rs. {demo_price:,} ---")
print(f"GST amount: Rs. {gst_on_item:,.2f}")

# --- Demo 5: Updating customer after payment ---
payment_received = 50000.00
customer["outstanding"] = customer["outstanding"] - payment_received
customer["last_payment_date"] = "09-Jul-2026"
customer["last_payment_amount"] = payment_received

print(f"\n--- After Payment of Rs. {payment_received:,.2f} ---")
print(f"  Outstanding now: Rs. {customer['outstanding']:,.2f}")
print(f"  Last payment   : Rs. {customer['last_payment_amount']:,.2f} on {customer['last_payment_date']}")

# --- Demo 6: Bank account dict with nested holder info ---
bank_account = {
    "account_no": "50123456789",
    "ifsc": "HDFC0001234",
    "branch": "FC Road, Pune",
    "holder": {
        "name": "Sharma Enterprises",
        "type": "Current",
        "pan": "AABCS5678C",
    },
    "balance": 342500.75,
}

print("\n--- Bank Account ---")
print(f"Account : {bank_account['account_no']} ({bank_account['holder']['type']})")
print(f"Holder  : {bank_account['holder']['name']}")
print(f"IFSC    : {bank_account['ifsc']}")
print(f"Balance : Rs. {bank_account['balance']:,.2f}")

# --- Demo 7: Count payment modes from list using dict as counter ---
payments = ["upi", "cash", "upi", "card", "upi", "neft", "cash", "upi"]
mode_count = {}
for mode in payments:
    mode_count[mode] = mode_count.get(mode, 0) + 1

print("\n--- Payment Mode Summary ---")
for mode, count in sorted(mode_count.items()):
    print(f"  {mode.upper():<6}: {count} transactions")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Dict product = {"name": "Desk", "price": 4500, "gst": 18}. Print name and price.
# Exercise 2: Add key "stock" = 25 to product. Print full dict.
# Exercise 3: ledger = {"Cash": 10000, "Bank": 50000}. Print total using values.

# --- Student code area ---
# product = {"name": "Desk", "price": 4500, "gst": 18}
# print(product["name"], product["price"])

# --- Solutions ---
# product["stock"] = 25
# print(product)
# ledger = {"Cash": 10000, "Bank": 50000}
# print(sum(ledger.values()))

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Build a complete sales receipt dict, compute totals, print formatted receipt.

print("\n--- MINI CHALLENGE: Sales Receipt Dict ---")
receipt = {
    "receipt_no": "SR-2026-1205",
    "shop": "City Mart",
    "cashier": "Anita",
    "datetime": "09-Jul-2026 14:32",
    "items": [
        {"name": "Bread", "qty": 2, "price": 45.00},
        {"name": "Butter 100g", "qty": 1, "price": 55.00},
        {"name": "Tea 250g", "qty": 1, "price": 120.00},
    ],
    "gst_inclusive": True,
}

subtotal = sum(item["qty"] * item["price"] for item in receipt["items"])

print(f"\n{receipt['shop']} — Receipt {receipt['receipt_no']}")
print(f"{receipt['datetime']} | Cashier: {receipt['cashier']}")
print("-" * 40)
for item in receipt["items"]:
    line_amt = item["qty"] * item["price"]
    print(f"{item['name']:<20} {item['qty']} x {item['price']:.2f} = {line_amt:.2f}")
print("-" * 40)
print(f"{'TOTAL (GST inclusive)':<30} Rs. {subtotal:.2f}")
print("Thank you — visit again!")
