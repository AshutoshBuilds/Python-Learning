"""
Lesson 36: Capstone — Expense Tracker
=====================================
Commerce focus: Summarize business expenses from CSV for budget reviews.
"""

import csv
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# csv.DictReader reads rows as dictionaries keyed by column headers.
# defaultdict simplifies grouping (e.g., totals per category).
# Compare actual spend against a budget dict to flag overspending.
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"
EXPENSES_CSV = DATA_DIR / "sample_expenses.csv"

# Monthly budget limits by category (Rs.)
BUDGET = {
    "Rent": 25000,
    "Utilities": 3500,
    "Salaries": 50000,
    "Inventory": 20000,
    "Marketing": 3000,
    "Transport": 2000,
    "Tax": 5000,
    "Bank Charges": 500,
    "Professional Fees": 8000,
}


def load_expenses(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def summarize_by_category(expenses: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for row in expenses:
        totals[row["category"]] += float(row["amount"])
    return dict(totals)


def find_top_expense(expenses: list[dict]) -> dict:
    return max(expenses, key=lambda r: float(r["amount"]))


def budget_vs_actual(category_totals: dict[str, float], budget: dict[str, float]) -> list[dict]:
    rows = []
    for category, actual in sorted(category_totals.items()):
        limit = budget.get(category, 0)
        variance = round(actual - limit, 2)
        status = "OVER" if actual > limit else "OK"
        rows.append(
            {
                "category": category,
                "budget": limit,
                "actual": actual,
                "variance": variance,
                "status": status,
            }
        )
    return rows


def print_dashboard(
    expenses: list[dict],
    category_totals: dict[str, float],
    budget_report: list[dict],
    top: dict,
) -> None:
    total_spend = sum(category_totals.values())
    print("=" * 55)
    print("EXPENSE TRACKER DASHBOARD")
    print("=" * 55)
    print(f"Records loaded : {len(expenses)}")
    print(f"Total spend    : Rs. {total_spend:,.2f}")
    print()
    print(f"{'Category':<22} {'Actual':>12} {'Budget':>12} {'Status':>8}")
    print("-" * 55)
    for row in budget_report:
        print(
            f"{row['category']:<22} {row['actual']:>12,.2f} "
            f"{row['budget']:>12,.2f} {row['status']:>8}"
        )
    print("-" * 55)
    print(
        f"\nTop single expense: Rs. {float(top['amount']):,.2f} — "
        f"{top['category']} ({top['vendor']}, {top['date']})"
    )


def main() -> None:
    # LIVE DEMOS
    expenses = load_expenses(EXPENSES_CSV)
    category_totals = summarize_by_category(expenses)
    top = find_top_expense(expenses)
    budget_report = budget_vs_actual(category_totals, BUDGET)

    print("LIVE DEMO — Expense tracker from CSV")
    print_dashboard(expenses, category_totals, budget_report, top)

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Count how many expenses used UPI as payment_mode.
    # 2) List categories where actual exceeds budget by more than Rs. 1000.
    #
    # Solution 1:
    #   upi_count = sum(1 for e in expenses if e["payment_mode"] == "UPI")
    #
    # Solution 2:
    #   overs = [r for r in budget_report if r["variance"] > 1000]
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Filter expenses for February only and print a separate mini-dashboard.


if __name__ == "__main__":
    main()
