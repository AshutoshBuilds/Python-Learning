"""
Lesson 20: Modules and Packages
===============================
Goals:
  - Import and use standard library modules: math, datetime, random, decimal.
  - Round money safely with Decimal; compute EMI with math.pow.
  - Understand why commerce scripts reuse tested library code.

Why commerce cares:
  Loans need EMI formulas, invoices need dates and rounding, simulations
  need random samples — the standard library provides this without Excel.
"""

USE_INPUT = False

import math
import random
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

# ---------------------------------------------------------------------------
# CONCEPT: import module  |  from module import name
# Packages are folders of modules. Standard library ships with Python.
# decimal.Decimal avoids float rounding surprises on money (e.g. 0.1 + 0.2).
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 20 — MODULES & PACKAGES")
print("=" * 60)


def money(value):
    """Round to 2 decimal places using banker's half-up."""
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def emi(principal, annual_rate_pct, months):
    """
    EMI = P × r × (1+r)^n / ((1+r)^n - 1)
    r = monthly rate (annual / 12 / 100)
    Uses math.pow for (1+r)^n
    """
    p = float(principal)
    r = annual_rate_pct / 12 / 100
    n = int(months)
    if r == 0:
        return round(p / n, 2)
    factor = math.pow(1 + r, n)
    payment = p * r * factor / (factor - 1)
    return round(payment, 2)


# ---------------------------------------------------------------------------
# LIVE DEMO 1 — math: EMI and compound factor
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: EMI with math.pow ---")

loan = 500000
rate = 10.5
tenure_months = 36

monthly_emi = emi(loan, rate, tenure_months)
total_paid = round(monthly_emi * tenure_months, 2)
total_interest = round(total_paid - loan, 2)

print(f"Loan amount     : Rs {loan:,}")
print(f"Interest rate   : {rate}% p.a.")
print(f"Tenure          : {tenure_months} months")
print(f"EMI             : Rs {monthly_emi:,.2f}")
print(f"Total repayment : Rs {total_paid:,.2f}")
print(f"Total interest  : Rs {total_interest:,.2f}")

# math helpers for quick checks
print(f"sqrt of 2       : {math.sqrt(2):.6f}")
print(f"ceil(4.2)       : {math.ceil(4.2)}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — decimal: GST without float drift
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Decimal for GST ---")

taxable = Decimal("1234.50")
gst_rate = Decimal("0.18")
gst = money(taxable * gst_rate)
total = money(taxable + gst)

# Compare with float (can show tiny errors)
float_gst = 1234.50 * 0.18
print(f"Taxable (Decimal): Rs {taxable}")
print(f"GST (Decimal)    : Rs {gst}")
print(f"Total            : Rs {total}")
print(f"GST (float raw)  : {float_gst}  <- may show long decimals")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — datetime: invoice due dates and payment terms
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: datetime — payment terms ---")

invoice_date = date(2026, 1, 15)
credit_days = 30
due_date = invoice_date + timedelta(days=credit_days)
today = date(2026, 2, 10)

days_remaining = (due_date - today).days
status = "OVERDUE" if days_remaining < 0 else "DUE SOON" if days_remaining <= 5 else "OK"

print(f"Invoice date : {invoice_date.isoformat()}")
print(f"Due date     : {due_date.isoformat()} (Net {credit_days})")
print(f"Today        : {today.isoformat()}")
print(f"Days left    : {days_remaining} -> {status}")

# Timestamp for audit log
logged_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Logged at    : {logged_at}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — random: simulate daily cash counter deposits
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: random — simulated deposits ---")

random.seed(42)  # reproducible demo
deposit_days = 7
daily_deposits = [random.randint(8000, 18000) for _ in range(deposit_days)]
week_total = sum(daily_deposits)

print(f"{'Day':>4} {'Deposit':>10}")
print("-" * 16)
for day, amt in enumerate(daily_deposits, start=1):
    print(f"{day:>4} {amt:>10,}")
print("-" * 16)
print(f"{'Week':>4} {week_total:>10,}")

sample_invoice = random.choice(["INV-1001", "INV-1002", "INV-1003"])
print(f"Random audit pick: {sample_invoice}")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — Combining modules in a mini ledger entry
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Combined module usage ---")

entries = [
    {"desc": "Sale", "amount": "15600.00"},
    {"desc": "Refund", "amount": "-1200.50"},
    {"desc": "Sale", "amount": "8900.25"},
]

balance = Decimal("0")
for entry in entries:
    balance += Decimal(entry["amount"])

balance = money(balance)
print(f"Ledger balance: Rs {balance}")
print(f"Abs value (math.fabs): {math.fabs(float(balance)):.2f}")

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Use math.pow(1.075, 5) to grow Rs 100000 at 7.5% for 5 years.")
print("2. Print date.today() + timedelta(weeks=2) as invoice follow-up date.")
print("3. Use Decimal('99.99') * 3 and money() for line total.")

# Solution 1:
# fv = 100000 * math.pow(1.075, 5)

# Solution 2:
# follow_up = date.today() + timedelta(weeks=2)

# Solution 3:
# line = money(Decimal("99.99") * 3)

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Compute EMI for Rs 8,00,000 at 9% for 60 months; "
    "use Decimal for total interest paid (total - principal)."
)

challenge_principal = 800000
challenge_rate = 9.0
challenge_months = 60
challenge_emi = emi(challenge_principal, challenge_rate, challenge_months)
challenge_total = money(Decimal(str(challenge_emi)) * challenge_months)
challenge_interest = money(challenge_total - Decimal(str(challenge_principal)))

print(f"  EMI            : Rs {challenge_emi:,.2f}")
print(f"  Total interest : Rs {challenge_interest}")

if USE_INPUT:
    p = float(input("Loan principal: ") or "100000")
    r = float(input("Rate %: ") or "10")
    m = int(input("Months: ") or "12")
    print(f"Your EMI: Rs {emi(p, r, m):,.2f}")

print("\nLesson 20 complete.")
print("Next up: Object-oriented Python (classes for Invoice, Customer, …).")
