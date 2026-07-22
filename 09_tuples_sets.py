"""
Lesson 09: Tuples and Sets
Learning goals: Tuples as immutable business records; sets for unique SKUs and invoice IDs.
Why commerce cares: A posted journal entry or GST invoice line should not change (tuple).
                    Duplicate SKU codes or invoice numbers cause inventory and audit chaos (set).
"""

# =============================================================================
# CONCEPT
# =============================================================================
# TUPLE — ordered, IMMUTABLE (cannot change after creation):
#   invoice_header = ("INV-001", "09-Jul-2026", 50000.00)
#   Access like lists: invoice_header[0], invoice_header[-1]
#   Use when data must stay fixed: coordinates, DB row snapshot, GST line item
#
# SET — unordered collection of UNIQUE items:
#   skus = {"SKU-A", "SKU-B", "SKU-A"}  → only one "SKU-A"
#   Operations: add(), remove(), in, union |, intersection &
#   Use for: unique product codes, distinct customers today, deduplicating IDs
#
# CREATE SET FROM LIST:
#   duplicate_ids = [101, 102, 101, 103]
#   unique_ids = set(duplicate_ids)   → {101, 102, 103}

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("TUPLES & SETS — RECORDS AND UNIQUE IDs")
print("=" * 50)

# --- Demo 1: Tuple as immutable invoice header record ---
invoice_record = (
    "INV-2026-0441",      # invoice number
    "09-Jul-2026",        # date
    "Horizon Traders",    # buyer
    "27AABCH1234F1Z5",    # buyer GSTIN
    125000.00,            # taxable value
    22500.00,             # total GST
    147500.00,            # grand total
)

print("\n--- Invoice Record (Tuple) ---")
print(f"Invoice No : {invoice_record[0]}")
print(f"Date       : {invoice_record[1]}")
print(f"Buyer      : {invoice_record[2]}")
print(f"GSTIN      : {invoice_record[3]}")
print(f"Taxable    : Rs. {invoice_record[4]:,.2f}")
print(f"GST        : Rs. {invoice_record[5]:,.2f}")
print(f"Grand Total: Rs. {invoice_record[6]:,.2f}")
print(f"Fields in record: {len(invoice_record)}")

# Tuple unpacking — assign multiple variables at once
inv_no, inv_date, buyer, gstin, taxable, gst, total = invoice_record
print(f"\nUnpacked -> {buyer} owes Rs. {total:,.2f} on {inv_no}")

# --- Demo 2: Tuple of line items (nested tuples) ---
line_items = (
    ("Notebook A4", "4820", 10, 65.00),
    ("Ball Pen Blue", "9608", 50, 8.00),
    ("Stapler", "8305", 2, 185.00),
)

print("\n--- Line Items (Tuple of Tuples) ---")
print(f"{'Item':<18} {'HSN':<6} {'Qty':>5} {'Rate':>8} {'Amount':>10}")
print("-" * 52)
for item in line_items:
    name, hsn, qty, rate = item
    amount = qty * rate
    print(f"{name:<18} {hsn:<6} {qty:>5} {rate:>8.2f} {amount:>10.2f}")

# --- Demo 3: Sets — unique SKUs in warehouse ---
warehouse_skus = {"SKU-001", "SKU-002", "SKU-003", "SKU-001", "SKU-004"}
print(f"\n--- Unique SKUs ({len(warehouse_skus)} items) ---")
for sku in sorted(warehouse_skus):
    print(f"  {sku}")

# --- Demo 4: Deduplicate invoice IDs from a messy import ---
raw_invoice_ids = [
    "INV-100", "INV-101", "INV-100", "INV-102",
    "INV-101", "INV-103", "INV-100",
]
unique_invoices = set(raw_invoice_ids)

print(f"\n--- Invoice ID Deduplication ---")
print(f"Raw count    : {len(raw_invoice_ids)}")
print(f"Unique count : {len(unique_invoices)}")
print(f"Unique IDs   : {sorted(unique_invoices)}")

# --- Demo 5: Set operations — products sold today vs yesterday ---
sold_today = {"Pen", "Notebook", "Eraser", "Marker", "Notebook"}
sold_yesterday = {"Pen", "Glue", "Notebook", "Scissors"}

both_days = sold_today & sold_yesterday       # intersection
only_today = sold_today - sold_yesterday       # difference
all_products = sold_today | sold_yesterday    # union

print("\n--- Sales Comparison (Sets) ---")
print(f"Sold today     : {sold_today}")
print(f"Sold yesterday : {sold_yesterday}")
print(f"Both days      : {both_days}")
print(f"Only today     : {only_today}")
print(f"All unique     : {all_products}")

# --- Demo 6: Checking membership — valid payment modes ---
valid_modes = {"cash", "upi", "card", "neft", "cheque"}
attempted_mode = "upi"
print(f"\n'{attempted_mode}' valid payment mode? {attempted_mode in valid_modes}")

# --- Demo 7: Frozen record — bank transaction tuple ---
txn = ("09-Jul-2026", "CR", "NEFT-IN", 25000.00, "REF-88421")
txn_date, txn_type, mode, amount, ref = txn
print(f"\nBank txn: {txn_date} | {txn_type} | {mode} | Rs. {amount:,.2f} | {ref}")

# --- Demo 8: Adding new SKU to set ---
new_skus = {"SKU-005", "SKU-002"}   # SKU-002 already exists
warehouse_skus = warehouse_skus | new_skus
print(f"\nWarehouse after import: {len(warehouse_skus)} unique SKUs")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Create tuple t = ("GST", 18, "INTRA"). Print element 1 and len(t).
# Exercise 2: From list [1,2,2,3,3,3] make a set. Print it and its length.
# Exercise 3: Sets a={1,2,3}, b={3,4,5}. Print intersection and union.

# --- Student code area ---
# t = ("GST", 18, "INTRA")
# print(t[1], len(t))

# --- Solutions ---
# dup = [1, 2, 2, 3, 3, 3]
# s = set(dup)
# print(s, len(s))
# a, b = {1, 2, 3}, {3, 4, 5}
# print(a & b, a | b)

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Two salespeople submitted customer lists (with duplicates). Find unique customers
# each served exclusively, and total unique customers.

print("\n--- MINI CHALLENGE: Sales Territory Overlap ---")
rep_a_customers = [
    "Mehta Ltd", "Shah Traders", "Patel Stores",
    "Mehta Ltd", "Gupta & Co", "Shah Traders",
]
rep_b_customers = [
    "Patel Stores", "Singh Enterprises", "Mehta Ltd",
    "Singh Enterprises", "Jain Distributors",
]

set_a = set(rep_a_customers)
set_b = set(rep_b_customers)
only_a = set_a - set_b
only_b = set_b - set_a
shared = set_a & set_b
total_unique = set_a | set_b

print(f"Rep A unique only : {only_a}")
print(f"Rep B unique only : {only_b}")
print(f"Shared customers  : {shared}")
print(f"Total unique      : {len(total_unique)} customers")
