"""
Lesson 18: Error Handling — try / except / else / finally
=========================================================
Goals:
  - Catch predictable failures without crashing batch jobs.
  - Handle ZeroDivisionError on margin, ValueError on bad amounts.
  - Safely parse user or CSV text into floats.

Why commerce cares:
  Bad spreadsheet cells, empty revenue rows, and mistyped amounts are normal.
  Robust scripts log the problem and continue processing other invoices.
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT:
#   try: risky code
#   except SomeError: handle it
#   else: runs if NO exception in try
#   finally: always runs (cleanup)
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 18 — ERROR HANDLING")
print("=" * 60)


def safe_margin_percent(profit_amount, revenue):
    """Return margin %; avoid crash when revenue is zero."""
    try:
        margin = (profit_amount / revenue) * 100
    except ZeroDivisionError:
        return None  # undefined margin
    else:
        return round(margin, 2)


def parse_amount(text):
    """Convert text to float; return None if invalid."""
    try:
        value = float(text)
    except ValueError:
        return None
    else:
        if value < 0:
            return None  # business rule: reject negatives
        return round(value, 2)


def apply_discount(price, discount_pct):
    try:
        if discount_pct < 0 or discount_pct > 100:
            raise ValueError("discount out of range")
        return round(price * (1 - discount_pct / 100), 2)
    except ValueError as err:
        print(f"  Discount error: {err}")
        return price


# ---------------------------------------------------------------------------
# LIVE DEMO 1 — ZeroDivisionError on margin
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Safe margin calculation ---")

scenarios = [
    ("Normal month", 15000, 60000),
    ("Loss month", -2000, 40000),
    ("Zero revenue", 5000, 0),
]

for label, profit_amt, revenue in scenarios:
    margin = safe_margin_percent(profit_amt, revenue)
    if margin is None:
        print(f"  {label}: margin undefined (revenue is zero)")
    else:
        print(f"  {label}: margin {margin}%")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — ValueError on bad amount strings
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Safe float parse ---")

raw_inputs = ["12500.50", "9,800", "abc", "", "-500", "0.18"]

for raw in raw_inputs:
    cleaned = raw.replace(",", "")  # simple cleanup before parse
    amount = parse_amount(cleaned)
    if amount is None:
        print(f"  '{raw}' -> REJECTED (invalid or negative)")
    else:
        print(f"  '{raw}' -> Rs {amount:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — try/except/else/finally in file-style batch
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Process batch with error isolation ---")

batch_rows = [
    {"id": "ROW-1", "revenue": "50000", "cost": "32000"},
    {"id": "ROW-2", "revenue": "N/A", "cost": "10000"},
    {"id": "ROW-3", "revenue": "8000", "cost": "0"},
    {"id": "ROW-4", "revenue": "12000", "cost": "15000"},
]

processed = 0
errors = 0

for row in batch_rows:
    try:
        revenue = float(row["revenue"])
        cost = float(row["cost"])
        margin = safe_margin_percent(revenue - cost, revenue)
        if margin is None:
            raise ZeroDivisionError("zero revenue")
    except (ValueError, ZeroDivisionError) as exc:
        errors += 1
        print(f"  {row['id']}: FAILED ({exc.__class__.__name__})")
    else:
        processed += 1
        print(f"  {row['id']}: margin {margin}%")
    finally:
        pass  # placeholder: could close file handles here

print(f"Batch done — OK: {processed}, errors: {errors}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Raising and catching business rule errors
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Discount validation ---")

for pct in (10, 150, -5):
    result = apply_discount(1000, pct)
    print(f"  Discount {pct}% -> payable Rs {result:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — Multiple except blocks
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Interest calculator with typed errors ---")

def interest_per_month(principal, rate_pct, months):
    try:
        principal = float(principal)
        rate_pct = float(rate_pct)
        months = int(months)
        if months <= 0:
            raise ValueError("months must be positive")
        monthly = principal * (rate_pct / 100) / 12 * months
    except ValueError as e:
        return f"Input error: {e}"
    except TypeError:
        return "Input error: wrong type"
    else:
        return round(monthly, 2)


tests = [
    (100000, 12, 6),
    ("100000", "12", "6"),
    (100000, 12, 0),
    (100000, "high", 6),
]
for args in tests:
    print(f"  interest_per_month{args} = {interest_per_month(*args)}")

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Wrap int('42a') in try/except and print a friendly message.")
print("2. Write safe_divide(a, b) returning None when b is 0.")
print("3. Use else to print 'Parsed OK' only when float() succeeds.")

# Solution 1:
# try:
#     int("42a")
# except ValueError:
#     print("Not a valid integer")

# Solution 2:
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None

# Solution 3:
# try:
#     v = float("99.5")
# except ValueError:
#     pass
# else:
#     print("Parsed OK", v)

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Parse amounts ['1000', '2,500.50', 'FREE', '750'] into floats; "
    "sum only valid values; report count skipped."
)

challenge_raw = ["1000", "2,500.50", "FREE", "750"]
valid_sum = 0
skipped = 0
for item in challenge_raw:
    val = parse_amount(item.replace(",", ""))
    if val is None:
        skipped += 1
    else:
        valid_sum += val
print(f"  Valid sum: Rs {valid_sum:,.2f}  |  Skipped: {skipped}")

if USE_INPUT:
    user_amt = input("Enter invoice amount: ")
    print(f"Parsed: {parse_amount(user_amt)}")

print("\nLesson 18 complete.")
