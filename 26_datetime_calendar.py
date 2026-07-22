"""
Lesson 26: datetime & timedelta
===============================
Work with invoice dates, due dates, and aging buckets for receivables.
Critical for accounts receivable and payment follow-up.

Run: python 26_datetime_calendar.py
"""

from datetime import datetime, timedelta, date

# =============================================================================
# CONCEPT
# =============================================================================
# datetime — date + time (e.g. invoice timestamp)
# date     — calendar date only
# timedelta — duration (e.g. 30 days credit period)
#
# Operations:
#   due_date = invoice_date + timedelta(days=30)
#   days_overdue = (today - due_date).days
#
# Aging buckets (common in AR reports):
#   0-30 days   — current
#   31-60 days  — follow up
#   60+ days    — serious overdue

print("=" * 60)
print("LESSON 26: datetime & timedelta")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

def make_invoice(invoice_id, customer, amount, invoice_date, credit_days=30):
    """Return invoice dict with computed due date."""
    due = invoice_date + timedelta(days=credit_days)
    return {
        "invoice_id": invoice_id,
        "customer": customer,
        "amount": amount,
        "invoice_date": invoice_date,
        "due_date": due,
        "credit_days": credit_days,
    }


def days_outstanding(invoice_date, as_of):
    """How many days since invoice was raised."""
    return (as_of - invoice_date).days


def aging_bucket(invoice_date, as_of):
    """Classify receivable into aging bucket."""
    days = days_outstanding(invoice_date, as_of)
    if days <= 30:
        return "0-30"
    if days <= 60:
        return "31-60"
    return "60+"


def format_date(d):
    return d.strftime("%d-%b-%Y")


# --- Demo: Create invoice with due date ---
print("\n--- Invoice Date & Due Date ---")
inv_date = date(2026, 1, 15)
inv = make_invoice("INV-1004", "Sharma Traders", 12500.0, inv_date, credit_days=30)
print(f"Invoice:  {inv['invoice_id']}")
print(f"Customer: {inv['customer']}")
print(f"Amount:   Rs {inv['amount']:,.2f}")
print(f"Inv date: {format_date(inv['invoice_date'])}")
print(f"Due date: {format_date(inv['due_date'])}")
print(f"Credit:   {inv['credit_days']} days")

# --- Demo: timedelta arithmetic ---
print("\n--- timedelta Arithmetic ---")
today = date(2026, 2, 20)
days_to_due = (inv["due_date"] - today).days
if days_to_due >= 0:
    print(f"Due in {days_to_due} days")
else:
    print(f"Overdue by {abs(days_to_due)} days")

# --- Demo: datetime for timestamps ---
print("\n--- datetime for Timestamps ---")
recorded_at = datetime(2026, 1, 15, 14, 30, 0)
print(f"Invoice recorded: {recorded_at.strftime('%d-%b-%Y %I:%M %p')}")
end_of_day = recorded_at.replace(hour=23, minute=59, second=59)
print(f"End of business day: {end_of_day.strftime('%H:%M:%S')}")

# --- Demo: Aging report ---
print("\n--- Aging Buckets (Receivables) ---")
as_of = date(2026, 2, 20)
receivables = [
    ("INV-1001", "Sharma Traders", 8500.0, date(2026, 1, 5)),
    ("INV-1003", "Patel Retail", 7200.0, date(2026, 1, 12)),
    ("INV-1006", "Mehta Bank Supplies", 15000.0, date(2025, 12, 1)),
    ("INV-1008", "Gupta & Co", 4200.0, date(2026, 2, 1)),
]

bucket_totals = {"0-30": 0.0, "31-60": 0.0, "60+": 0.0}

print(f"{'Invoice':<12} {'Customer':<22} {'Amount':>10} {'Days':>6} {'Bucket':>8}")
print("-" * 62)
for inv_id, cust, amt, inv_dt in receivables:
    days = days_outstanding(inv_dt, as_of)
    bucket = aging_bucket(inv_dt, as_of)
    bucket_totals[bucket] += amt
    print(f"{inv_id:<12} {cust:<22} {amt:>10,.2f} {days:>6} {bucket:>8}")

print("-" * 62)
print("Bucket summary:")
for bucket, total in bucket_totals.items():
    print(f"  {bucket:>6} days: Rs {total:,.2f}")

# --- Demo: Parse date from string ---
print("\n--- Parsing Dates from CSV-style Strings ---")
csv_date = "2026-01-22"
parsed = datetime.strptime(csv_date, "%Y-%m-%d").date()
print(f"Parsed '{csv_date}' -> {format_date(parsed)}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Invoice dated 2026-02-01, 45-day credit. Print due date.

# inv_d = date(2026, 2, 1)
# due = inv_d + timedelta(days=45)
# print(format_date(due))

# Exercise 2: As of 2026-03-15, how many days outstanding for 2026-01-20 invoice?

# print(days_outstanding(date(2026, 1, 20), date(2026, 3, 15)))

# Exercise 3: Which bucket for invoice date 2025-11-01 as of 2026-02-01?

# print(aging_bucket(date(2025, 11, 1), date(2026, 2, 1)))


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
Build a mini AR dashboard:
  1. Three unpaid invoices with different dates.
  2. As-of date: 2026-02-28.
  3. Print each invoice's days outstanding and bucket.
  4. Print total amount in the 60+ bucket only.
""")

# --- Mini challenge reference solution ---
challenge_invoices = [
    ("INV-2001", 5000.0, date(2026, 2, 10)),
    ("INV-2002", 8000.0, date(2025, 12, 15)),
    ("INV-2003", 3200.0, date(2026, 1, 25)),
]
as_of_challenge = date(2026, 2, 28)
over_60_total = 0.0

print("\nChallenge result:")
for inv_id, amt, inv_dt in challenge_invoices:
    days = days_outstanding(inv_dt, as_of_challenge)
    bucket = aging_bucket(inv_dt, as_of_challenge)
    print(f"  {inv_id}: {days} days -> {bucket}")
    if bucket == "60+":
        over_60_total += amt

print(f"  Total in 60+ bucket: Rs {over_60_total:,.2f}")

print("\nLesson 26 complete.")
