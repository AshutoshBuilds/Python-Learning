"""
Lesson 15: Functions — Advanced
===============================
Goals:
  - Default parameter values for optional business rules.
  - *args and **kwargs for flexible invoice totals.
  - Local vs global scope; avoid accidental shadowing.

Why commerce cares:
  Invoices mix line items, discounts, shipping, and GST slabs.
  Flexible functions adapt to each client without rewriting core logic.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: defaults, *args (tuple of extras), **kwargs (dict of named extras)
# Scope: variables inside a function are local unless declared global.
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 15 — FUNCTIONS (ADVANCED)")
print("=" * 60)

SHOP_GST_DEFAULT = 0.18  # module-level constant


def line_total(qty, unit_price, discount_pct=0, gst_rate=SHOP_GST_DEFAULT):
    """Compute one invoice line with optional discount and GST."""
    gross = qty * unit_price
    discount = round(gross * discount_pct / 100, 2)
    taxable = gross - discount
    gst = round(taxable * gst_rate, 2)
    return {
        "gross": gross,
        "discount": discount,
        "taxable": taxable,
        "gst": gst,
        "total": taxable + gst,
    }


def sum_line_totals(*lines):
    """*args: pass any number of numeric line totals."""
    return round(sum(lines), 2)


def flexible_invoice_total(subtotal, *extra_charges, **adjustments):
    """
    extra_charges: positional add-ons (shipping, packaging)
    adjustments: named kwargs — discount=500, rebate=100, etc.
    """
    total = subtotal + sum(extra_charges)
    for label, amount in adjustments.items():
        total -= amount
        print(f"  Applied {label}: -Rs {amount:,.2f}")
    return round(max(total, 0), 2)


# ---------------------------------------------------------------------------
# LIVE DEMO 1 — Default parameters on invoice lines
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Defaults for discount and GST ---")

lines = [
    (10, 120),                    # no discount, default GST
    (5, 80, 5),                   # 5% discount
    (3, 450, 0, 0.18),            # explicit GST
    (20, 350, 2, 0.05),           # grocery slab
]

for i, args in enumerate(lines, start=1):
    result = line_total(*args)
    print(
        f"  Line {i}: gross Rs {result['gross']:,}  "
        f"disc Rs {result['discount']:.2f}  "
        f"total Rs {result['total']:.2f}"
    )

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — *args: variable number of credit notes
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Sum credits with *args ---")

credit_note_1 = 1200
credit_note_2 = 450
credit_note_3 = 800
total_credits = sum_line_totals(credit_note_1, credit_note_2, credit_note_3)
print(f"  Credits applied: Rs {total_credits:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — **kwargs: flexible invoice adjustments
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Flexible invoice total ---")

base_subtotal = 28500
final = flexible_invoice_total(
    base_subtotal,
    350,   # shipping (extra charge)
    150,   # packaging (extra charge)
    trade_discount=2000,
    loyalty_rebate=500,
)
print(f"  Subtotal Rs {base_subtotal:,} -> Payable Rs {final:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Scope: local counter vs global setting
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Scope demo ---")

transaction_count = 0  # global-style module variable


def record_sale(amount):
    global transaction_count
    transaction_count += 1
    fee = round(amount * 0.02, 2)  # local variable
    return fee


for sale_amt in (5000, 12000, 800):
    fee = record_sale(sale_amt)
    print(f"  Sale Rs {sale_amt:,} -> platform fee Rs {fee:.2f}")

print(f"  Transactions recorded: {transaction_count}")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — Combining *args and **kwargs in a report helper
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Report header builder ---")

def build_report_header(title, *tags, **meta):
    header = f"=== {title} ==="
    if tags:
        header += f"  [{', '.join(tags)}]"
    for key, val in meta.items():
        header += f"\n  {key.replace('_', ' ').title()}: {val}"
    return header


print(build_report_header(
    "Monthly GST Summary",
    "GSTR-1",
    "Draft",
    period="Jan 2026",
    prepared_by="Accounts Team",
))

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Write apply_fees(base, *fees) returning base + sum of fees.")
print("2. Write price_after(**kwargs) reading 'amount' and 'discount_pct'.")
print("3. Why should you avoid mutable defaults like def f(items=[])? ")

# Solution 1:
# def apply_fees(base, *fees):
#     return round(base + sum(fees), 2)

# Solution 2:
# def price_after(**kwargs):
#     amt = kwargs.get("amount", 0)
#     disc = kwargs.get("discount_pct", 0)
#     return round(amt * (1 - disc / 100), 2)

# Solution 3:
# Mutable default is shared across calls; use None and create list inside.

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Build invoice_grand_total(subtotal, *surcharges, **deductions) "
    "and compute for subtotal 50000, surcharges 1200 & 800, "
    "deductions early_payment=1500, volume_discount=3000."
)


def invoice_grand_total(subtotal, *surcharges, **deductions):
    total = subtotal + sum(surcharges)
    for name, value in deductions.items():
        total -= value
    return round(max(total, 0), 2)


challenge_total = invoice_grand_total(
    50000, 1200, 800,
    early_payment=1500,
    volume_discount=3000,
)
print(f"  Grand total payable: Rs {challenge_total:,.2f}")

if USE_INPUT:
    extra = input("Add a note tag for report: ")
    print(build_report_header("Custom Report", extra))

print("\nLesson 15 complete.")
