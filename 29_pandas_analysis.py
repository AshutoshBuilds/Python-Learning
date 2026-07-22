"""
Lesson 29: pandas Analysis — groupby & Pivot-style Aggregations
=================================================================
NOTE: pip install pandas

Group sales by category, compute revenue and profit sketch,
pivot-style summaries for management reporting.

Run: python 29_pandas_analysis.py
"""

import sys
from pathlib import Path

# =============================================================================
# CONCEPT
# =============================================================================
# groupby — split data into groups, apply aggregation, combine results
#
#   df.groupby("category")["line_total"].sum()
#   df.pivot_table(values="line_total", index="category", aggfunc="sum")
#
# Profit sketch = revenue - estimated cost (here we assume 70% of subtotal
# is cost for demo purposes — real P&L uses actual COGS).

print("=" * 60)
print("LESSON 29: pandas Analysis")
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

df = pd.read_csv(DATA_PATH)
df["line_subtotal"] = df["qty"] * df["unit_price"]
df["gst_amount"] = (df["line_subtotal"] * df["gst_rate"]).round(2)
df["line_total"] = (df["line_subtotal"] + df["gst_amount"]).round(2)

# Assumed cost ratio for profit sketch (commerce teaching demo)
COST_RATIO = 0.70
df["estimated_cost"] = (df["line_subtotal"] * COST_RATIO).round(2)
df["gross_profit"] = (df["line_subtotal"] - df["estimated_cost"]).round(2)

# --- groupby: revenue by category ---
print("\n--- Revenue by Category (groupby) ---")
category_revenue = df.groupby("category")["line_total"].sum().sort_values(ascending=False)
for cat, rev in category_revenue.items():
    print(f"  {cat:15} Rs {rev:>12,.2f}")

# --- groupby: multiple aggregations ---
print("\n--- Category Summary (multiple metrics) ---")
category_summary = df.groupby("category").agg(
    lines=("product", "count"),
    units_sold=("qty", "sum"),
    revenue=("line_total", "sum"),
    gst_collected=("gst_amount", "sum"),
    gross_profit=("gross_profit", "sum"),
).round(2)
print(category_summary)

# --- pivot_table style ---
print("\n--- Pivot Table: Revenue by Category ---")
pivot_revenue = pd.pivot_table(
    df,
    values="line_total",
    index="category",
    aggfunc="sum",
    margins=True,
    margins_name="TOTAL",
)
print(pivot_revenue)

# --- Customer-wise revenue ---
print("\n--- Top Customers by Revenue ---")
customer_revenue = (
    df.groupby("customer")["line_total"]
    .sum()
    .sort_values(ascending=False)
)
for cust, rev in customer_revenue.items():
    print(f"  {cust:25} Rs {rev:,.2f}")

# --- Profit sketch P&L ---
print("\n--- Profit Sketch (P&L Summary) ---")
total_revenue_ex_gst = df["line_subtotal"].sum()
total_cost = df["estimated_cost"].sum()
total_gross_profit = df["gross_profit"].sum()
total_gst = df["gst_amount"].sum()

print(f"  Revenue (ex-GST):   Rs {total_revenue_ex_gst:,.2f}")
print(f"  Est. COGS (70%):    Rs {total_cost:,.2f}")
print(f"  Gross Profit:       Rs {total_gross_profit:,.2f}")
print(f"  GST (liability):    Rs {total_gst:,.2f}")
print(f"  Total billed:       Rs {df['line_total'].sum():,.2f}")

# --- Monthly trend (parse date) ---
print("\n--- Monthly Revenue ---")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")
monthly = df.groupby("month")["line_total"].sum()
for month, rev in monthly.items():
    print(f"  {month}: Rs {rev:,.2f}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: groupby category — find average unit_price per category.

# avg_price = df.groupby("category")["unit_price"].mean().round(2)
# print(avg_price)

# Exercise 2: Which category has the highest total qty sold?

# qty_by_cat = df.groupby("category")["qty"].sum()
# print(qty_by_cat.idxmax(), qty_by_cat.max())

# Exercise 3: pivot_table — gst_amount sum by category.

# gst_pivot = pd.pivot_table(df, values="gst_amount", index="category", aggfunc="sum")
# print(gst_pivot)


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
Build a management snapshot:
  1. Best category by gross_profit (not revenue).
  2. Worst category by gross_profit.
  3. Overall gross margin % = gross_profit / line_subtotal * 100
  4. Print all three numbers.
""")

# --- Mini challenge reference solution ---
profit_by_cat = df.groupby("category")["gross_profit"].sum()
best_cat = profit_by_cat.idxmax()
worst_cat = profit_by_cat.idxmin()
overall_margin = (df["gross_profit"].sum() / df["line_subtotal"].sum()) * 100

print("\nChallenge result:")
print(f"  Best category:  {best_cat} (Rs {profit_by_cat[best_cat]:,.2f} profit)")
print(f"  Worst category: {worst_cat} (Rs {profit_by_cat[worst_cat]:,.2f} profit)")
print(f"  Gross margin:   {overall_margin:.1f}%")

print("\nLesson 29 complete.")
