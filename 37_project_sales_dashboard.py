"""
Lesson 37: Capstone — Sales Dashboard
=====================================
Commerce focus: Summarize sales by customer and category from CSV data.
"""

import csv
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# pandas (if installed) makes grouping and aggregation easy with groupby.
# Without pandas, use csv + defaultdict — same results, more manual code.
# Dashboard = printed summary tables for quick business decisions.
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"
SALES_CSV = DATA_DIR / "sample_sales.csv"


def load_sales_csv(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8", newline="") as f:
        rows = []
        for row in csv.DictReader(f):
            row["qty"] = int(row["qty"])
            row["unit_price"] = float(row["unit_price"])
            row["gst_rate"] = float(row["gst_rate"])
            row["line_total"] = round(
                row["qty"] * row["unit_price"] * (1 + row["gst_rate"]), 2
            )
            rows.append(row)
        return rows


def summarize_stdlib(rows: list[dict]) -> tuple[dict, dict, float]:
    by_customer: dict[str, float] = defaultdict(float)
    by_category: dict[str, float] = defaultdict(float)
    for row in rows:
        by_customer[row["customer"]] += row["line_total"]
        by_category[row["category"]] += row["line_total"]
    grand_total = sum(r["line_total"] for r in rows)
    return dict(by_customer), dict(by_category), grand_total


def summarize_pandas(csv_path: Path) -> tuple[dict, dict, float]:
    import pandas as pd

    df = pd.read_csv(csv_path)
    df["line_total"] = df["qty"] * df["unit_price"] * (1 + df["gst_rate"])
    by_customer = df.groupby("customer")["line_total"].sum().round(2).to_dict()
    by_category = df.groupby("category")["line_total"].sum().round(2).to_dict()
    grand_total = round(float(df["line_total"].sum()), 2)
    return by_customer, by_category, grand_total


def print_table(title: str, data: dict[str, float]) -> None:
    print(f"\n{title}")
    print("-" * 40)
    for key, value in sorted(data.items(), key=lambda x: -x[1]):
        print(f"  {key:<25} Rs. {value:>10,.2f}")


def print_dashboard(
    by_customer: dict[str, float],
    by_category: dict[str, float],
    grand_total: float,
    engine: str,
) -> None:
    print("=" * 55)
    print("SALES DASHBOARD")
    print("=" * 55)
    print(f"Data engine : {engine}")
    print(f"Grand total : Rs. {grand_total:,.2f}")
    print_table("Sales by Customer", by_customer)
    print_table("Sales by Category", by_category)
    top_customer = max(by_customer, key=by_customer.get)
    print(f"\nTop customer: {top_customer} (Rs. {by_customer[top_customer]:,.2f})")


def main() -> None:
    # LIVE DEMOS — prefer pandas, fall back to csv/stdlib
    try:
        by_customer, by_category, grand_total = summarize_pandas(SALES_CSV)
        engine = "pandas"
    except (ImportError, ValueError, ModuleNotFoundError):
        rows = load_sales_csv(SALES_CSV)
        by_customer, by_category, grand_total = summarize_stdlib(rows)
        engine = "csv (stdlib)"

    print("LIVE DEMO — Sales dashboard")
    print_dashboard(by_customer, by_category, grand_total, engine)

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Find the product with the highest single line_total.
    # 2) Compute average invoice value (grand_total / unique invoice_ids).
    #
    # Solution 1 (stdlib):
    #   top = max(rows, key=lambda r: r["line_total"])
    #
    # Solution 2:
    #   invoices = {r["invoice_id"] for r in rows}
    #   avg = grand_total / len(invoices)
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Add a "Sales by Month" section by parsing the date column.


if __name__ == "__main__":
    main()
