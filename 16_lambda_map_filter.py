"""
Lesson 16: Lambda, map, filter, sorted
======================================
Goals:
  - Write small anonymous functions with lambda.
  - Transform lists with map, subset with filter, order with sorted.

Why commerce cares:
  Price lists need GST applied, unpaid bills filtered, and reports sorted
  by amount or due date — these one-liners keep data pipelines concise.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: lambda x: expression  (single expression, no statements)
# map(fn, iterable) -> transformed values
# filter(fn, iterable) -> items where fn returns True
# sorted(iterable, key=fn) -> ordered copy
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 16 — LAMBDA, MAP, FILTER, SORTED")
print("=" * 60)

GST_RATE = 0.18

# ---------------------------------------------------------------------------
# LIVE DEMO 1 — lambda: add GST to unit prices
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Price with GST (lambda) ---")

base_prices = [120, 299, 450, 890, 5000]

add_gst = lambda price: round(price * (1 + GST_RATE), 2)
# same as: def add_gst(price): return round(price * (1 + GST_RATE), 2)

print(f"{'Base':>8} {'With GST':>10}")
print("-" * 20)
for p in base_prices:
    print(f"{p:>8} {add_gst(p):>10.2f}")

# Using map:
prices_with_gst = list(map(add_gst, base_prices))
print(f"\nmap() result (first 3): {prices_with_gst[:3]}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — filter: unpaid invoices only
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Filter unpaid invoices ---")

invoices = [
    {"id": "INV-1001", "customer": "Sharma Traders", "amount": 5400, "paid": True},
    {"id": "INV-1002", "customer": "Patel Retail", "amount": 8200, "paid": False},
    {"id": "INV-1003", "customer": "Gupta & Co", "amount": 5900, "paid": False},
    {"id": "INV-1004", "customer": "Mehta Bank", "amount": 1350, "paid": True},
    {"id": "INV-1005", "customer": "Sharma Traders", "amount": 11200, "paid": False},
]

is_unpaid = lambda inv: not inv["paid"]
unpaid = list(filter(is_unpaid, invoices))

print(f"Total invoices: {len(invoices)}  |  Unpaid: {len(unpaid)}")
for inv in unpaid:
    print(f"  {inv['id']}: {inv['customer']} owes Rs {inv['amount']:,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — sorted: order by amount (descending)
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Sort invoices by amount ---")

by_amount_desc = sorted(invoices, key=lambda x: x["amount"], reverse=True)
print(f"{'ID':<10} {'Customer':<18} {'Amount':>10}")
print("-" * 42)
for inv in by_amount_desc:
    print(f"{inv['id']:<10} {inv['customer']:<18} {inv['amount']:>10,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — map + lambda: compute line totals from tuples
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: map line totals (qty × price) ---")

order_lines = [(10, 120), (5, 80), (3, 450), (8, 299)]
line_totals = list(map(lambda pair: pair[0] * pair[1], order_lines))
print(f"Line totals: {line_totals}")
print(f"Order subtotal: Rs {sum(line_totals):,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — filter high-value + sort by customer name
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: High-value unpaid, sorted by customer ---")

HIGH_VALUE = 5000
high_unpaid = filter(
    lambda inv: (not inv["paid"]) and inv["amount"] >= HIGH_VALUE,
    invoices,
)
sorted_high = sorted(high_unpaid, key=lambda inv: inv["customer"])
for inv in sorted_high:
    print(f"  Follow up: {inv['customer']} — Rs {inv['amount']:,}")

# ---------------------------------------------------------------------------
# LIVE DEMO 6 — map for GST components on taxable amounts
# ---------------------------------------------------------------------------
print("\n--- DEMO 6: GST component extraction ---")

taxable_amounts = [1000, 2500, 7800]
gst_only = list(map(lambda t: round(t * GST_RATE, 2), taxable_amounts))
print(list(zip(taxable_amounts, gst_only)))

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Use filter to keep bank deposits > 5000 from [3000, 12000, 800, 9000].")
print("2. Use sorted to order customers ['Zed', 'Amy', 'Mohan'] alphabetically.")
print("3. map(lambda x: x * 1.05, [100, 200]) for 5% price hike.")

# Solution 1:
# deposits = [3000, 12000, 800, 9000]
# big = list(filter(lambda d: d > 5000, deposits))

# Solution 2:
# sorted(["Zed", "Amy", "Mohan"])

# Solution 3:
# list(map(lambda x: x * 1.05, [100, 200]))

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "From invoices, produce a list of (id, amount_with_18pct_gst) "
    "for unpaid only, sorted by amount_with_gst descending."
)

challenge = sorted(
    map(
        lambda inv: (inv["id"], round(inv["amount"] * 1.18, 2)),
        filter(lambda inv: not inv["paid"], invoices),
    ),
    key=lambda pair: pair[1],
    reverse=True,
)
for inv_id, total in challenge:
    print(f"  {inv_id}: Rs {total:,.2f} (incl. GST)")

if USE_INPUT:
    thresh = float(input("Min amount filter: ") or "5000")
    custom = list(filter(lambda i: i["amount"] >= thresh, invoices))
    print(f"Matching: {len(custom)}")

print("\nLesson 16 complete.")
