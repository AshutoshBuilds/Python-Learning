"""
Lesson 17: List Comprehensions
==============================
Goals:
  - Build lists in one readable expression: [expr for item in seq if condition].
  - Compute taxable amounts, overdue flags, and filtered business lists.

Why commerce cares:
  Reports often need "all amounts over X" or "flag overdue accounts" in one pass.
  Comprehensions are faster to read than manual append loops for simple cases.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: [expression for item in iterable if condition]
# Dict comp: {k: v for ...}  |  Set comp: {x for ...}
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 17 — LIST COMPREHENSIONS")
print("=" * 60)

# ---------------------------------------------------------------------------
# LIVE DEMO 1 — Taxable amounts from invoice lines
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Taxable amounts ---")

lines = [
    {"product": "Pen", "qty": 50, "price": 12, "exempt": False},
    {"product": "Milk", "qty": 20, "price": 55, "exempt": True},
    {"product": "Book", "qty": 10, "price": 120, "exempt": False},
    {"product": "Rice", "qty": 15, "price": 350, "exempt": False},
]

taxable_amounts = [
    line["qty"] * line["price"]
    for line in lines
    if not line["exempt"]
]

print(f"Taxable line amounts: {taxable_amounts}")
print(f"Total taxable: Rs {sum(taxable_amounts):,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — Overdue flags from days past due
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Overdue flags ---")

accounts = [
    {"name": "Sharma Traders", "days_past_due": 0},
    {"name": "Patel Retail", "days_past_due": 12},
    {"name": "Gupta & Co", "days_past_due": 35},
    {"name": "Mehta Bank Supplies", "days_past_due": 45},
    {"name": "Singh Enterprises", "days_past_due": 5},
]

OVERDUE_DAYS = 30

overdue_flags = [
    {
        "name": acc["name"],
        "overdue": acc["days_past_due"] > OVERDUE_DAYS,
        "days": acc["days_past_due"],
    }
    for acc in accounts
]

for row in overdue_flags:
    status = "OVERDUE" if row["overdue"] else "OK"
    print(f"  {row['name']:<22} {row['days']:>3} days -> {status}")

overdue_names = [row["name"] for row in overdue_flags if row["overdue"]]
print(f"\nSend reminders to: {overdue_names}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — GST-inclusive prices (with expression transform)
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: GST-inclusive price list ---")

unit_prices = [120, 299, 450, 80]
gst_rate = 0.18
inclusive = [round(p * (1 + gst_rate), 2) for p in unit_prices]
print(f"Base:      {unit_prices}")
print(f"Incl GST:  {inclusive}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Nested comprehension: branch × target check
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Branches below sales target ---")

branches = ["Mumbai", "Delhi", "Pune"]
sales = [92000, 105000, 78000]
target = 85000

below_target = [
    (branch, sale)
    for branch, sale in zip(branches, sales)
    if sale < target
]
for branch, sale in below_target:
    gap = target - sale
    print(f"  {branch}: Rs {sale:,} (short by Rs {gap:,})")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — Dict comprehension: invoice id -> total
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Dict comprehension ---")

raw_orders = [("INV-101", 4500), ("INV-102", 8200), ("INV-103", 1200)]
order_map = {inv_id: amt for inv_id, amt in raw_orders}
print(order_map)

# ---------------------------------------------------------------------------
# LIVE DEMO 6 — Set comprehension: unique GST slabs in catalog
# ---------------------------------------------------------------------------
print("\n--- DEMO 6: Unique GST slabs ---")

catalog = [
    {"item": "Rice", "gst": 0.05},
    {"item": "Pen", "gst": 0.12},
    {"item": "Laptop", "gst": 0.18},
    {"item": "Oil", "gst": 0.05},
    {"item": "Book", "gst": 0.12},
]

slabs = {round(item["gst"] * 100) for item in catalog}
print(f"GST slabs in catalog: {sorted(slabs)}%")

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. [x * 2 for x in [100, 250, 400]] — double list prices.")
print("2. [c for c in customers if c.startswith('S')] — filter names.")
print("3. Build [(name, days) for ...] where overdue only (days > 30).")

# Solution 1:
# doubled = [x * 2 for x in [100, 250, 400]]

# Solution 2:
# customers = ["Sharma", "Patel", "Singh", "Gupta"]
# s_names = [c for c in customers if c.startswith("S")]

# Solution 3:
# overdue_pairs = [(a["name"], a["days_past_due"]) for a in accounts if a["days_past_due"] > 30]

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Given sales [12500, 9800, 14300, 7200, 15600], "
    "build a list of 'Day N: Rs X (HIGH)' only for sales >= 12000."
)

daily_sales = [12500, 9800, 14300, 7200, 15600]
high_days = [
    f"Day {i}: Rs {amt:,} (HIGH)"
    for i, amt in enumerate(daily_sales, start=1)
    if amt >= 12000
]
for entry in high_days:
    print(f"  {entry}")

if USE_INPUT:
    t = int(input("Overdue threshold days: ") or "30")
    custom = [a["name"] for a in accounts if a["days_past_due"] > t]
    print(f"Overdue at {t} days: {custom}")

print("\nLesson 17 complete.")
