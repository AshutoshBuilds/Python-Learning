"""
Lesson 19: Files — Text and CSV
===============================
Goals:
  - Read and write plain text files for logs and exports.
  - Use the csv module for spreadsheet-friendly sales data.
  - Resolve paths relative to this lesson file with pathlib.

Why commerce cares:
  Sales registers, bank statements, and GST exports are often CSV or text.
  Python can automate "read yesterday's file, summarise, write report".
"""

USE_INPUT = False

import csv
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT: open(path, mode)  modes: 'r' read, 'w' write, 'a' append
# csv.reader / csv.DictReader for tabular data
# Path(__file__).parent locates files next to the lesson script
# ---------------------------------------------------------------------------

print("=" * 60)
print("LESSON 19 — FILES (TEXT & CSV)")
print("=" * 60)

LESSON_DIR = Path(__file__).parent
DATA_DIR = LESSON_DIR / "data"
SAMPLE_CSV = DATA_DIR / "sample_sales.csv"
LESSON_TEMP = LESSON_DIR / "_lesson19_temp_sales.csv"


def resolve_sales_csv():
    """Prefer bundled sample_sales.csv; else create a tiny demo file."""
    if SAMPLE_CSV.exists():
        return SAMPLE_CSV
    demo_rows = [
        ["date", "invoice_id", "customer", "qty", "unit_price", "gst_rate"],
        ["2026-01-05", "INV-9001", "Demo Traders", "5", "100", "0.12"],
        ["2026-01-08", "INV-9002", "Sample Retail", "2", "450", "0.18"],
    ]
    LESSON_TEMP.write_text(
        "\n".join(",".join(row) for row in demo_rows) + "\n",
        encoding="utf-8",
    )
    print(f"  (Created demo CSV at {LESSON_TEMP.name})")
    return LESSON_TEMP


# ---------------------------------------------------------------------------
# LIVE DEMO 1 — Write and read a plain text payment log
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: Text file write/read ---")

log_path = LESSON_DIR / "_lesson19_payment_log.txt"
payments = [
    "2026-02-01 | INV-1001 | Sharma Traders | Rs 5,400",
    "2026-02-03 | INV-1002 | Patel Retail   | Rs 8,200",
    "2026-02-05 | INV-1003 | Gupta & Co     | Rs 5,900",
]

with open(log_path, "w", encoding="utf-8") as f:
    f.write("PAYMENT LOG\n")
    f.write("=" * 40 + "\n")
    for line in payments:
        f.write(line + "\n")

print(f"Wrote {len(payments)} lines to {log_path.name}")

with open(log_path, "r", encoding="utf-8") as f:
    content = f.read()
    line_count = len(content.strip().splitlines())
print(f"Read back {line_count} lines from log.")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — Read CSV with csv.DictReader
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Read sample_sales.csv ---")

csv_path = resolve_sales_csv()
print(f"Using: {csv_path}")

rows = []
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

print(f"Loaded {len(rows)} sales row(s).")
print(f"Columns: {list(rows[0].keys()) if rows else []}")

# Show first 3 rows
for row in rows[:3]:
    print(
        f"  {row.get('invoice_id', '?')}: "
        f"{row.get('product', row.get('customer', 'item'))} "
        f"qty {row.get('qty', '?')}"
    )

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — Compute revenue per invoice from CSV
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Revenue by invoice ---")

invoice_totals = {}
for row in rows:
    inv_id = row.get("invoice_id", "UNKNOWN")
    try:
        qty = float(row.get("qty", 0))
        price = float(row.get("unit_price", 0))
        gst_rate = float(row.get("gst_rate", 0))
    except ValueError:
        continue
    line_taxable = qty * price
    line_total = round(line_taxable * (1 + gst_rate), 2)
    invoice_totals[inv_id] = invoice_totals.get(inv_id, 0) + line_total

print(f"{'Invoice':<12} {'Total (incl GST)':>18}")
print("-" * 32)
for inv_id in sorted(invoice_totals):
    print(f"{inv_id:<12} {invoice_totals[inv_id]:>18,.2f}")

grand_total = sum(invoice_totals.values())
print("-" * 32)
print(f"{'GRAND TOTAL':<12} {grand_total:>18,.2f}")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Write summary CSV export
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: Write summary CSV ---")

export_path = LESSON_DIR / "_lesson19_invoice_summary.csv"
with open(export_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["invoice_id", "total_incl_gst"])
    for inv_id in sorted(invoice_totals):
        writer.writerow([inv_id, f"{invoice_totals[inv_id]:.2f}"])

print(f"Exported {len(invoice_totals)} invoice(s) to {export_path.name}")

# Verify by reading back
with open(export_path, newline="", encoding="utf-8") as f:
    exported = list(csv.reader(f))
print(f"Verification: {len(exported) - 1} data row(s) in export.")

# ---------------------------------------------------------------------------
# LIVE DEMO 5 — Append mode for daily audit trail
# ---------------------------------------------------------------------------
print("\n--- DEMO 5: Append audit line ---")

audit_path = LESSON_DIR / "_lesson19_audit.txt"
audit_path.write_text("AUDIT TRAIL\n", encoding="utf-8")
with open(audit_path, "a", encoding="utf-8") as f:
    f.write(f"Processed {len(rows)} rows from {csv_path.name}\n")
    f.write(f"Grand total Rs {grand_total:,.2f}\n")

print(audit_path.read_text(encoding="utf-8").strip())

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Count how many rows have category 'Grocery' (if column exists).")
print("2. Write a CSV with columns customer, total_spent (aggregate by customer).")
print("3. Use Path.exists() before opening a file; print friendly error if missing.")

# Solution 1:
# grocery_count = sum(1 for r in rows if r.get("category") == "Grocery")

# Solution 2:
# by_customer = {}
# for row in rows:
#     cust = row["customer"]
#     qty, price = float(row["qty"]), float(row["unit_price"])
#     by_customer[cust] = by_customer.get(cust, 0) + qty * price

# Solution 3:
# p = Path("missing.csv")
# if not p.exists():
#     print("File not found")

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "Find the customer with highest total spend across all rows "
    "(qty × unit_price, ignore GST for simplicity)."
)

customer_spend = {}
for row in rows:
    cust = row.get("customer", "Unknown")
    try:
        spend = float(row["qty"]) * float(row["unit_price"])
    except (KeyError, ValueError):
        continue
    customer_spend[cust] = customer_spend.get(cust, 0) + spend

if customer_spend:
    top_customer = max(customer_spend, key=customer_spend.get)
    print(
        f"  Top customer: {top_customer} "
        f"(Rs {customer_spend[top_customer]:,.2f})"
    )

if USE_INPUT:
    fname = input("Enter CSV filename to check: ")
    check = DATA_DIR / fname
    print(f"Exists: {check.exists()}")

print("\nLesson 19 complete.")
