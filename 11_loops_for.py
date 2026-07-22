"""
Lesson 11: For Loops
====================
Goals:
  - Use for loops to repeat work over sequences (lists, ranges, strings).
  - Sum sales, walk invoice lines, and track a running total.

Why commerce cares:
  Accountants process many invoices, line items, and daily sales totals.
  A for loop lets you automate "do this for every row" without copy-paste errors.
"""

USE_INPUT = False  # Set True only if you want interactive prompts in class.

# ---------------------------------------------------------------------------
# CONCEPT: for item in sequence
# ---------------------------------------------------------------------------
# A for loop visits each element once, in order.
# range(n) gives 0, 1, 2, ... n-1 — useful for counting quarters or months.
# running_total += value is the standard pattern for cumulative sums.

print("=" * 60)
print("LESSON 11 — FOR LOOPS")
print("=" * 60)

# ---------------------------------------------------------------------------
# LIVE DEMO 1 — Sum daily sales from a list
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Sum daily sales ---")

daily_sales = [12500, 9800, 14300, 11200, 15600]  # rupees per day (Mon–Fri)

total_week_sales = 0
for amount in daily_sales:
    total_week_sales += amount
    print(f"  Added Rs {amount:,}  ->  running total Rs {total_week_sales:,}")

print(f"Weekly sales total: Rs {total_week_sales:,}")
avg_daily = total_week_sales / len(daily_sales)
print(f"Average daily sales: Rs {avg_daily:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — Iterate invoice lines (qty × price + GST)
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Invoice line items ---")

GST_RATE = 0.18
invoice_lines = [
    {"product": "Ledger Book", "qty": 10, "unit_price": 120},
    {"product": "Pen Box", "qty": 5, "unit_price": 80},
    {"product": "Calculator", "qty": 3, "unit_price": 450},
]

invoice_subtotal = 0
print(f"{'Product':<16} {'Qty':>4} {'Rate':>8} {'Line Amt':>12}")
print("-" * 44)

for line in invoice_lines:
    line_amount = line["qty"] * line["unit_price"]
    invoice_subtotal += line_amount
    print(
        f"{line['product']:<16} {line['qty']:>4} "
        f"{line['unit_price']:>8} {line_amount:>12}"
    )

gst_amount = round(invoice_subtotal * GST_RATE, 2)
invoice_total = invoice_subtotal + gst_amount
print("-" * 44)
print(f"Subtotal: Rs {invoice_subtotal:,}  |  GST @18%: Rs {gst_amount:,.2f}")
print(f"Invoice total: Rs {invoice_total:,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — Running total until a target (monthly revenue tracker)
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Running total toward monthly target ---")

TARGET_REVENUE = 50000
monthly_inflows = [8200, 11500, 9400, 13200, 7800, 10100]

cumulative = 0
for day_num, inflow in enumerate(monthly_inflows, start=1):
    cumulative += inflow
    pct = (cumulative / TARGET_REVENUE) * 100
    print(
        f"  Day {day_num}: +Rs {inflow:,}  |  "
        f"Cumulative Rs {cumulative:,} ({pct:.1f}% of target)"
    )

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Loop over a string (validate invoice ID format)
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Check invoice ID characters ---")

invoice_id = "INV-1001"
digit_count = 0
for ch in invoice_id:
    if ch.isdigit():
        digit_count += 1
print(f"Invoice '{invoice_id}' contains {digit_count} digit(s).")

# ---------------------------------------------------------------------------
# EXERCISES (try yourself first; solutions below in comments)
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Sum only sales above Rs 10,000 from daily_sales.")
print("2. Print each product name in UPPERCASE from invoice_lines.")
print("3. Use range(1, 13) to print 'Month N budget: Rs 25000' for 12 months.")

# Solution 1:
# high_sales_total = 0
# for amount in daily_sales:
#     if amount > 10000:
#         high_sales_total += amount
# print(high_sales_total)

# Solution 2:
# for line in invoice_lines:
#     print(line["product"].upper())

# Solution 3:
# for month in range(1, 13):
#     print(f"Month {month} budget: Rs 25000")

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Given bank credits [4500, 12000, 800, 22000, 650], "
    "print each credit and stop the loop once cumulative credits exceed Rs 30,000."
)

# Reference solution for the challenge (students should try first):
bank_credits = [4500, 12000, 800, 22000, 650]
running = 0
for credit in bank_credits:
    running += credit
    print(f"  Credit Rs {credit:,} -> total Rs {running:,}")
    if running > 30000:
        print("  Target exceeded — stopping early.")
        break

if USE_INPUT:
    name = input("Your name for certificate tracking: ")
    print(f"Great work, {name}!")

print("\nLesson 11 complete.")
