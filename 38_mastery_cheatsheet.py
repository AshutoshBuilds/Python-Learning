"""
Lesson 38: Python Mastery Cheatsheet
====================================
Commerce focus: Quick revision of patterns used across this course.
"""

from typing import Union

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# A cheatsheet collects small, working snippets you can re-run anytime.
# Each section prints a label and demonstrates one core pattern.
# Use this file before exams or when starting a new commerce project.
# ---------------------------------------------------------------------------

SECTION_BREAK = "-" * 50


def section(title: str) -> None:
    print(f"\n{SECTION_BREAK}\n{title}\n{SECTION_BREAK}")


def demo_variables_and_types() -> None:
    section("1. Variables & Types")
    shop_name = "Sharma Traders"
    gst_rate = 0.18
    is_registered = True
    print(f"  shop_name     = {shop_name!r}  (str)")
    print(f"  gst_rate      = {gst_rate}     (float)")
    print(f"  is_registered = {is_registered}   (bool)")


def demo_gst_one_liner() -> None:
    section("2. GST One-Liner")
    amount = 1000
    gst = round(amount * 0.18, 2)
    total = amount + gst
    print(f"  taxable = Rs. {amount}")
    print(f"  gst     = Rs. {gst}")
    print(f"  total   = Rs. {total}")


def demo_dict_ledger() -> None:
    section("3. Dict Ledger")
    ledger = {"Cash": 50000, "Bank": 120000, "Sales": 170000}
    ledger["Cash"] -= 25000  # rent payment
    print(f"  ledger = {ledger}")
    print(f"  net assets (Cash+Bank) = Rs. {ledger['Cash'] + ledger['Bank']:,}")


def demo_function() -> None:
    section("4. Function")

    def simple_interest(p: float, r: float, t: float) -> float:
        return round(p * r * t / 100, 2)

    si = simple_interest(10000, 8, 2)
    print(f"  SI on Rs. 10,000 @ 8% for 2 yrs = Rs. {si:,}")


def demo_class_stub() -> None:
    section("5. Class Stub")

    class Product:
        def __init__(self, name: str, price: float) -> None:
            self.name = name
            self.price = price

        def with_gst(self, rate: float = 0.18) -> float:
            return round(self.price * (1 + rate), 2)

    item = Product("Calculator", 450)
    print(f"  {item.name} MRP incl. GST = Rs. {item.with_gst():,.2f}")


def demo_try_except() -> None:
    section("6. try / except")

    def safe_divide(a: float, b: float) -> Union[float, str]:
        try:
            return round(a / b, 2)
        except ZeroDivisionError:
            return "Cannot divide by zero"

    print(f"  100 / 4 = {safe_divide(100, 4)}")
    print(f"  100 / 0 = {safe_divide(100, 0)}")


def demo_file_and_path() -> None:
    section("7. Path & File (pattern)")
    from pathlib import Path

    data_file = Path(__file__).parent / "data" / "sample_expenses.csv"
    exists = data_file.exists()
    print(f"  Path: {data_file.name}")
    print(f"  Exists: {exists}")


def demo_list_comprehension() -> None:
    section("8. List Comprehension")
    prices = [120, 80, 450, 299]
    with_gst = [round(p * 1.18, 2) for p in prices]
    print(f"  prices   = {prices}")
    print(f"  with GST = {with_gst}")


def main() -> None:
    print("=" * 50)
    print("PYTHON MASTERY CHEATSHEET — Commerce Edition")
    print("=" * 50)

    # LIVE DEMOS — all sections
    demo_variables_and_types()
    demo_gst_one_liner()
    demo_dict_ledger()
    demo_function()
    demo_class_stub()
    demo_try_except()
    demo_file_and_path()
    demo_list_comprehension()

    print(f"\n{SECTION_BREAK}")
    print("Revision complete. Re-run anytime before projects or tests.")
    print(SECTION_BREAK)

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Add a section "9. for loop" that prints first 3 multiples of GST 18%.
    # 2) Add a section showing f-string formatting for currency.
    #
    # Solution 1:
    #   for i in range(1, 4):
    #       print(round(1000 * i * 0.18, 2))
    #
    # Solution 2:
    #   amount = 12345.6
    #   print(f"Rs. {amount:,.2f}")
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Copy your three favourite snippets into a personal notes file
    # and modify them for your own shop scenario.


if __name__ == "__main__":
    main()
