"""
Lesson 31: Data Visualization with Matplotlib
==============================================
Commerce focus: Plot monthly revenue to spot trends for business reviews.

NOTE: pip install matplotlib
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# Matplotlib draws charts from numbers in Python lists or CSV files.
# For scripts (no pop-up window), use the Agg backend so figures save to PNG.
# Bar charts compare categories (months); line charts show trends over time.
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"
CHART_PATH = DATA_DIR / "revenue_chart_demo.png"

# Hardcoded monthly revenue (Rs.) — typical small retail shop
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
REVENUE = [185000, 212000, 198500, 225000, 241000, 236500]


def load_revenue_from_csv(csv_path: Path) -> tuple[list[str], list[float]]:
    """Optional: read month,revenue from a two-column CSV."""
    months: list[str] = []
    amounts: list[float] = []
    with csv_path.open(encoding="utf-8") as f:
        next(f)  # skip header
        for line in f:
            month, amount = line.strip().split(",")
            months.append(month)
            amounts.append(float(amount))
    return months, amounts


def main() -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")  # non-interactive backend — no display needed
        import matplotlib.pyplot as plt
    except (ImportError, AttributeError, ModuleNotFoundError):
        print("matplotlib is not installed or failed to load.")
        print("Run: pip install matplotlib")
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    months = MONTHS
    revenue = REVENUE

    # LIVE DEMOS — bar chart and line chart on one figure
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    fig.suptitle("Monthly Revenue — Demo Shop FY 2025-26", fontsize=12)

    axes[0].bar(months, revenue, color="steelblue", edgecolor="navy")
    axes[0].set_title("Bar Chart — Revenue by Month")
    axes[0].set_ylabel("Revenue (Rs.)")
    axes[0].tick_params(axis="x", rotation=45)

    axes[1].plot(months, revenue, marker="o", color="darkgreen", linewidth=2)
    axes[1].set_title("Line Chart — Revenue Trend")
    axes[1].set_ylabel("Revenue (Rs.)")
    axes[1].grid(True, alpha=0.3)
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    fig.savefig(CHART_PATH, dpi=120, bbox_inches="tight")
    plt.close(fig)

    total = sum(revenue)
    best_month = months[revenue.index(max(revenue))]
    print("LIVE DEMO — Revenue charts saved")
    print(f"  File : {CHART_PATH}")
    print(f"  Total revenue (6 months): Rs. {total:,.0f}")
    print(f"  Best month: {best_month} (Rs. {max(revenue):,.0f})")

    # -----------------------------------------------------------------------
    # EXERCISES — try yourself first; solutions below in comments
    # -----------------------------------------------------------------------
    # 1) Add a third subplot showing average revenue as a horizontal line.
    # 2) Change bar colours for months below average to grey.
    #
    # Solution 1 (concept):
    #   avg = total / len(revenue)
    #   axes[1].axhline(avg, color="red", linestyle="--", label=f"Avg {avg:,.0f}")
    #
    # Solution 2 (concept):
    #   colors = ["steelblue" if r >= avg else "grey" for r in revenue]
    #   axes[0].bar(months, revenue, color=colors)
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Create data/monthly_revenue.csv with your own 6 months, load it with
    # load_revenue_from_csv(), and regenerate the chart from that file.


if __name__ == "__main__":
    main()
