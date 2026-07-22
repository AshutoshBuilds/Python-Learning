"""
Lesson 24: Decorators & Generators
==================================
Decorators wrap functions to add behaviour (logging, timing).
Generators yield values lazily — perfect for EMI schedules.

Run: python 24_decorators_generators.py
"""

# =============================================================================
# CONCEPT
# =============================================================================
# DECORATOR: a function that takes a function and returns an enhanced version.
#   @log_call
#   def calc_gst(...): ...
#
# GENERATOR: uses `yield` instead of `return` — produces one value at a time.
#   for month, emi in emi_schedule(...): ...
#
# Commerce use:
#   Log every tax calculation for audit trail
#   Stream monthly EMI breakdown without storing full list in memory

print("=" * 60)
print("LESSON 24: Decorators & Generators")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

def log_tax_calc(func):
    """Decorator: log function name, inputs, and result."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"  [TAX LOG] {func.__name__}(args={args}, kwargs={kwargs}) -> {result}")
        return result

    return wrapper


@log_tax_calc
def calculate_gst(taxable_amount, gst_rate):
    """Compute GST amount on a taxable base."""
    return round(taxable_amount * gst_rate, 2)


@log_tax_calc
def calculate_invoice_total(lines, gst_rate):
    """Sum line amounts and add GST."""
    subtotal = sum(lines)
    gst = round(subtotal * gst_rate, 2)
    return round(subtotal + gst, 2)


def emi_schedule(principal, annual_rate, months):
    """
    Generator: yield (month_number, emi, interest_part, principal_part, balance)
    for a reducing-balance loan (business term loan / vehicle loan).
    """
    monthly_rate = annual_rate / 12 / 100
    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = principal * monthly_rate * (1 + monthly_rate) ** months
        emi /= (1 + monthly_rate) ** months - 1
    emi = round(emi, 2)

    balance = principal
    for month in range(1, months + 1):
        interest = round(balance * monthly_rate, 2)
        principal_part = round(emi - interest, 2)
        balance = round(max(balance - principal_part, 0), 2)
        yield month, emi, interest, principal_part, balance


def gst_summary_generator(invoices):
    """Yield per-invoice GST summary dicts from a list of (id, taxable, rate)."""
    for inv_id, taxable, rate in invoices:
        gst = round(taxable * rate, 2)
        yield {
            "invoice_id": inv_id,
            "taxable": taxable,
            "gst_rate": rate,
            "gst_amount": gst,
            "total": round(taxable + gst, 2),
        }


# --- Demo: Decorator on tax functions ---
print("\n--- Decorator: Tax Calculation Logging ---")
gst_18 = calculate_gst(10000, 0.18)
total_bill = calculate_invoice_total([1200, 800, 450], gst_rate=0.12)
print(f"GST on 10,000 @ 18%: Rs {gst_18:,.2f}")
print(f"Invoice total: Rs {total_bill:,.2f}")

# --- Demo: Generator EMI schedule ---
print("\n--- Generator: Monthly EMI Schedule ---")
loan_amount = 500000
rate = 12.0
tenure = 6

print(f"Loan Rs {loan_amount:,.0f} @ {rate}% p.a. for {tenure} months\n")
print(f"{'Mo':>3} {'EMI':>10} {'Interest':>10} {'Principal':>10} {'Balance':>12}")
print("-" * 48)

for month, emi, interest, principal_part, balance in emi_schedule(loan_amount, rate, tenure):
    print(f"{month:>3} {emi:>10,.2f} {interest:>10,.2f} {principal_part:>10,.2f} {balance:>12,.2f}")

# --- Demo: GST summary generator ---
print("\n--- Generator: GST Summary Stream ---")
sample_invoices = [
    ("INV-1001", 1000.0, 0.12),
    ("INV-1002", 4500.0, 0.18),
    ("INV-1003", 350.0, 0.05),
]
for summary in gst_summary_generator(sample_invoices):
    print(
        f"  {summary['invoice_id']}: taxable Rs {summary['taxable']:,.2f} + "
        f"GST Rs {summary['gst_amount']:,.2f} = Rs {summary['total']:,.2f}"
    )


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Call calculate_gst(2500, 0.05) and observe the log line.

# calculate_gst(2500, 0.05)

# Exercise 2: Use emi_schedule for Rs 100000, 10% p.a., 3 months.
# Print only the last month's balance (should be ~0).

# last_balance = None
# for _, _, _, _, bal in emi_schedule(100000, 10.0, 3):
#     last_balance = bal
# print(f"Final balance: Rs {last_balance:,.2f}")

# Exercise 3: Write a tiny generator `count_up_to(n)` yielding 1..n.
# Sum GST rates applied in a loop over count_up_to(3) — just practice yield.

# def count_up_to(n):
#     for i in range(1, n + 1):
#         yield i
# print(list(count_up_to(3)))


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
1. Decorate a new function `calculate_tds(amount, rate)` that returns TDS deducted.
2. Run it for salary Rs 50000 at 10% TDS.
3. Generate EMI schedule for Rs 200000 @ 15% for 4 months.
4. Print total interest paid (sum of interest column).
""")

# --- Mini challenge reference solution ---

@log_tax_calc
def calculate_tds(amount, rate):
    return round(amount * rate, 2)


tds = calculate_tds(50000, 0.10)

total_interest = 0.0
for _, _, interest, _, _ in emi_schedule(200000, 15.0, 4):
    total_interest += interest

print(f"\nChallenge result:")
print(f"  TDS on Rs 50,000 @ 10%: Rs {tds:,.2f}")
print(f"  Total interest (4-month loan): Rs {total_interest:,.2f}")

print("\nLesson 24 complete.")
