"""
Lesson 14: Functions — Basics
=============================
Goals:
  - Define reusable functions with def, parameters, and return.
  - Build gst_amount(), simple_interest(), and profit() for commerce math.

Why commerce cares:
  GST, interest, and margin formulas repeat across invoices, loans, and P&L.
  Functions give one tested definition used everywhere — fewer manual errors.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: def name(params): ... return value
# ---------------------------------------------------------------------------
# Parameters are inputs; return sends a result back to the caller.
# Functions without return give None. Docstrings document business rules.

print("=" * 60)
print("LESSON 14 — FUNCTIONS (BASICS)")
print("=" * 60)


def gst_amount(taxable_value, rate=0.18):
    """GST in India is typically calculated on taxable value (pre-tax)."""
    return round(taxable_value * rate, 2)


def simple_interest(principal, rate_percent, years):
    """SI = P × R × T / 100  (R in percent, T in years)."""
    return round(principal * rate_percent * years / 100, 2)


def profit(revenue, cost):
    """Gross profit = revenue minus direct cost."""
    return round(revenue - cost, 2)


def profit_margin_percent(revenue, cost):
    """Margin % = profit / revenue × 100. Returns 0 if revenue is 0."""
    if revenue == 0:
        return 0.0
    return round((profit(revenue, cost) / revenue) * 100, 2)


# ---------------------------------------------------------------------------
# LIVE DEMO 1 — GST on invoice lines
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: GST helper ---")

line_items = [
    ("USB Drive", 8, 299, 0.18),
    ("Rice 5kg", 20, 350, 0.05),
    ("Ledger Book", 10, 120, 0.12),
]

print(f"{'Item':<14} {'Taxable':>10} {'GST':>10} {'Total':>10}")
print("-" * 48)

grand_taxable = 0
grand_gst = 0

for name, qty, price, rate in line_items:
    taxable = qty * price
    gst = gst_amount(taxable, rate)
    total = taxable + gst
    grand_taxable += taxable
    grand_gst += gst
    print(f"{name:<14} {taxable:>10,} {gst:>10.2f} {total:>10.2f}")

print("-" * 48)
print(f"{'TOTAL':<14} {grand_taxable:>10,} {grand_gst:>10.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — Simple interest on business loan
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Simple interest ---")

loan_principal = 500000
rate = 12.0  # 12% per annum
tenure = 2

interest = simple_interest(loan_principal, rate, tenure)
maturity = loan_principal + interest

print(f"Principal : Rs {loan_principal:,}")
print(f"Rate      : {rate}% p.a. for {tenure} year(s)")
print(f"Interest  : Rs {interest:,.2f}")
print(f"Maturity  : Rs {maturity:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — Profit and margin per product
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Profit per SKU ---")

products = [
    {"sku": "CALC-01", "selling": 550, "cost": 420},
    {"sku": "PEN-99", "selling": 25, "cost": 12},
    {"sku": "INK-44", "selling": 890, "cost": 710},
]

print(f"{'SKU':<10} {'Revenue':>8} {'Cost':>8} {'Profit':>8} {'Margin%':>8}")
print("-" * 46)

for p in products:
    rev = p["selling"]
    cst = p["cost"]
    prf = profit(rev, cst)
    margin = profit_margin_percent(rev, cst)
    print(f"{p['sku']:<10} {rev:>8} {cst:>8} {prf:>8.2f} {margin:>7.1f}%")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Functions calling functions
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Invoice total with GST ---")

def invoice_total_with_gst(lines):
    """lines: list of (qty, unit_price, gst_rate)"""
    subtotal = 0
    total_gst = 0
    for qty, price, rate in lines:
        taxable = qty * price
        subtotal += taxable
        total_gst += gst_amount(taxable, rate)
    return subtotal, total_gst, subtotal + total_gst


demo_lines = [(5, 80, 0.12), (3, 450, 0.18)]
sub, gst, total = invoice_total_with_gst(demo_lines)
print(f"Subtotal Rs {sub:,} + GST Rs {gst:.2f} = Rs {total:.2f}")

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Write discount_amount(price, pct) returning round(price * pct/100, 2).")
print("2. Write total_bill(amount, gst_rate) returning amount + gst_amount(...).")
print("3. Call simple_interest(100000, 8, 3) and print the result.")

# Solution 1:
# def discount_amount(price, pct):
#     return round(price * pct / 100, 2)

# Solution 2:
# def total_bill(amount, gst_rate):
#     return amount + gst_amount(amount, gst_rate)

# Solution 3:
# print(simple_interest(100000, 8, 3))  # 24000.0

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print("Define unit_profit(qty, sell_price, buy_price) and compute for 50 pens at 25/12.")

def unit_profit(qty, sell_price, buy_price):
    return profit(qty * sell_price, qty * buy_price)


challenge_result = unit_profit(50, 25, 12)
print(f"  Profit on 50 pens: Rs {challenge_result:,.2f}")

if USE_INPUT:
    p = float(input("Enter principal for SI demo: ") or "10000")
    print(f"SI @10% for 1 yr: Rs {simple_interest(p, 10, 1):,.2f}")

print("\nLesson 14 complete.")
