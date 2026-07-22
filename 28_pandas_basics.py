"""
Lesson 28: pandas Basics
========================
NOTE: pip install pandas

Load sales CSV, inspect data, filter rows, and compute line_total and GST.
Essential for commerce data analysis.

Run: python 28_pandas_basics.py
"""

import sys
from pathlib import Path

# =============================================================================
# CONCEPT
# =============================================================================
# pandas is the standard Python library for tabular data (like Excel sheets).
#
#   pd.read_csv(path)  — load CSV into DataFrame
#   df.head()          — first rows preview
#   df[df.col > 100]   — filter rows
#   df["new"] = ...    — add calculated column
#
# Commerce use:
#   Sales register, GST computation per line, category filters

print("=" * 60)
print("LESSON 28: pandas Basics")
print("=" * 60)

try:
    import pandas as pd
except (ImportError, ValueError) as err:
    print("\nERROR: pandas is not available.")
    print("Install with: pip install pandas")
    if isinstance(err, ValueError):
        print("Hint: if you see a numpy compatibility error, try:")
        print("  pip install --upgrade numpy pandas")
    print("Then re-run this lesson.")
    sys.exit(0)

# =============================================================================
# LIVE DEMOS
# =============================================================================

DATA_PATH = Path(__file__).parent / "data" / "sample_sales.csv"

if not DATA_PATH.exists():
    print(f"\nERROR: Data file not found: {DATA_PATH}")
    sys.exit(1)

# --- Load CSV ---
print(f"\n--- Loading {DATA_PATH.name} ---")
df = pd.read_csv(DATA_PATH)
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Columns: {list(df.columns)}")

# --- head() preview ---
print("\n--- df.head() ---")
print(df.head())

# --- Basic info ---
print("\n--- dtypes ---")
print(df.dtypes)

# --- Add calculated columns ---
print("\n--- New Columns: line_subtotal, gst_amount, line_total ---")
df["line_subtotal"] = df["qty"] * df["unit_price"]
df["gst_amount"] = (df["line_subtotal"] * df["gst_rate"]).round(2)
df["line_total"] = (df["line_subtotal"] + df["gst_amount"]).round(2)

print(df[["invoice_id", "product", "qty", "unit_price", "line_subtotal", "gst_amount", "line_total"]].head())

# --- Filter: Electronics only ---
print("\n--- Filter: category == 'Electronics' ---")
electronics = df[df["category"] == "Electronics"]
print(electronics[["invoice_id", "customer", "product", "line_total"]])

# --- Filter: high-value lines (line_total > 1000) ---
print("\n--- Filter: line_total > 1000 ---")
high_value = df[df["line_total"] > 1000]
print(high_value[["invoice_id", "product", "line_total"]].to_string(index=False))

# --- Filter: specific customer ---
print("\n--- Filter: Sharma Traders ---")
sharma_sales = df[df["customer"] == "Sharma Traders"]
print(f"Sharma Traders — {len(sharma_sales)} lines, total Rs {sharma_sales['line_total'].sum():,.2f}")

# --- Simple aggregates ---
print("\n--- Quick Aggregates ---")
print(f"Total revenue (incl. GST): Rs {df['line_total'].sum():,.2f}")
print(f"Total GST collected:       Rs {df['gst_amount'].sum():,.2f}")
print(f"Average line value:        Rs {df['line_total'].mean():,.2f}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Filter rows where category is "Grocery". Print product and qty.

# grocery = df[df["category"] == "Grocery"]
# print(grocery[["product", "qty"]])

# Exercise 2: Add column "unit_price_with_gst" = unit_price * (1 + gst_rate).

# df["unit_price_with_gst"] = (df["unit_price"] * (1 + df["gst_rate"])).round(2)
# print(df[["product", "unit_price", "unit_price_with_gst"]].head(3))

# Exercise 3: Count how many unique customers are in the dataset.

# print(f"Unique customers: {df['customer'].nunique()}")


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
1. Filter all "Services" category rows.
2. Compute total line_total for Services.
3. Find the single most expensive line (max line_total) — print product & amount.
""")

# --- Mini challenge reference solution ---
services = df[df["category"] == "Services"]
services_total = services["line_total"].sum()
top_line = df.loc[df["line_total"].idxmax()]

print("\nChallenge result:")
print(f"  Services revenue: Rs {services_total:,.2f}")
print(f"  Top line: {top_line['product']} — Rs {top_line['line_total']:,.2f}")

print("\nLesson 28 complete.")
