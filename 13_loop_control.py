"""
Lesson 13: Loop Control — break, continue, nested loops
=======================================================
Goals:
  - Skip unwanted records with continue.
  - Stop early when a target is met with break.
  - Nest loops for grids (products × branches) and invoice batches.

Why commerce cares:
  Real ledgers mix void invoices, partial payments, and branch-wise stock.
  break/continue let you process only valid rows and stop at budget caps.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: break exits the innermost loop; continue skips to next iteration.
# Nested loops: outer loop × inner loop (e.g., branches × products).
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 13 — LOOP CONTROL")
print("=" * 60)

# ---------------------------------------------------------------------------
# LIVE DEMO 1 — continue: skip void / cancelled invoices
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Skip void invoices (continue) ---")

invoices = [
    {"id": "INV-101", "amount": 4500, "status": "paid"},
    {"id": "INV-102", "amount": 0, "status": "void"},
    {"id": "INV-103", "amount": 8200, "status": "paid"},
    {"id": "INV-104", "amount": 1200, "status": "void"},
    {"id": "INV-105", "amount": 6700, "status": "pending"},
]

valid_total = 0
valid_count = 0

for inv in invoices:
    if inv["status"] == "void":
        print(f"  SKIP {inv['id']} (void)")
        continue
    valid_total += inv["amount"]
    valid_count += 1
    print(f"  COUNT {inv['id']}: Rs {inv['amount']:,}")

print(f"Valid invoices: {valid_count}  |  Revenue counted: Rs {valid_total:,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — break: stop when target revenue reached
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Stop at target revenue (break) ---")

TARGET = 25000
sales_queue = [5000, 8000, 12000, 6000, 9000, 4000]

running_revenue = 0
for i, sale in enumerate(sales_queue, start=1):
    running_revenue += sale
    print(f"  Sale {i}: +Rs {sale:,}  ->  Rs {running_revenue:,}")
    if running_revenue >= TARGET:
        print(f"  Monthly target Rs {TARGET:,} reached — stop processing.")
        break
else:
    # else on for-loop runs only if loop did NOT break
    print("  Target not reached with available sales.")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — nested loops: branches × product price list
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Nested loops — branch stock report ---")

branches = ["Mumbai", "Delhi", "Pune"]
products = ["Notebook", "Pen"]

print(f"{'Branch':<10}", end="")
for prod in products:
    print(f"{prod:>12}", end="")
print()
print("-" * 36)

stock = {
    ("Mumbai", "Notebook"): 120,
    ("Mumbai", "Pen"): 500,
    ("Delhi", "Notebook"): 80,
    ("Delhi", "Pen"): 300,
    ("Pune", "Notebook"): 60,
    ("Pune", "Pen"): 200,
}

for branch in branches:
    print(f"{branch:<10}", end="")
    for product in products:
        qty = stock.get((branch, product), 0)
        print(f"{qty:>12}", end="")
    print()

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — break in nested loop: find first overdue account
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Find first overdue account (nested + break) ---")

customers = [
    {"name": "Sharma Traders", "days_overdue": 0},
    {"name": "Patel Retail", "days_overdue": 15},
    {"name": "Gupta & Co", "days_overdue": 45},
    {"name": "Mehta Bank Supplies", "days_overdue": 5},
]

OVERDUE_THRESHOLD = 30
found = None

for cust in customers:
    for tier in (60, 45, 30, 15):  # check severity buckets
        if cust["days_overdue"] >= tier and tier == OVERDUE_THRESHOLD:
            found = cust
            break
    if found:
        break

if found:
    print(f"  First account >= {OVERDUE_THRESHOLD} days: {found['name']}")
else:
    print("  No account meets threshold.")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — continue + break together in payment matching
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Match payments to invoices ---")

open_invoices = [3000, 7500, 2000, 9000, 1500]
payments = [7500, 1000, 3000, 5000]
matched = 0

for payment in payments:
    if payment < 2000:
        print(f"  Skip small payment Rs {payment} (below minimum)")
        continue
    for inv_amt in open_invoices:
        if payment == inv_amt:
            print(f"  Matched payment Rs {payment} to invoice Rs {inv_amt}")
            matched += 1
            break
    if matched >= 2:
        print("  Reconciliation quota met for today.")
        break

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Sum positive bank entries only; skip negatives with continue.")
print("2. Print numbers 1–20 but break at 13 (unlucky for demo).")
print("3. Nested: for each GST slab (5%, 12%, 18%), print slab and 2 sample items.")

# Solution 1:
# entries = [500, -200, 1200, -50, 800]
# total = 0
# for e in entries:
#     if e < 0:
#         continue
#     total += e

# Solution 2:
# for n in range(1, 21):
#     if n == 13:
#         break
#     print(n)

# Solution 3:
# slabs = [0.05, 0.12, 0.18]
# items = [["Rice", "Oil"], ["Book", "Pen"], ["Laptop", "Scanner"]]
# for i, slab in enumerate(slabs):
#     print(f"GST {slab*100:.0f}%:", items[i])

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Process sales [4000, 0, 8000, 11000, 6000]. "
    "Skip zeros. Stop when cumulative >= 15000. Report how many sales counted."
)

challenge_sales = [4000, 0, 8000, 11000, 6000]
cum = 0
counted = 0
for s in challenge_sales:
    if s == 0:
        continue
    cum += s
    counted += 1
    if cum >= 15000:
        break
print(f"  Counted {counted} sale(s), cumulative Rs {cum:,}")

if USE_INPUT:
    ans = input("Which is safer: break or continue? ")
    print(f"You said: {ans}")

print("\nLesson 13 complete.")
