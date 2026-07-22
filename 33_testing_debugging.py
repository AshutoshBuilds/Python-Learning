"""
Lesson 33: Testing and Debugging
================================
Commerce focus: Verify GST and interest calculations before invoicing.
"""

import unittest

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# assert checks a condition and raises AssertionError if False — quick tests.
# unittest.TestCase groups related tests; run with python -m unittest or main().
# print-debugging: temporarily print variable values to trace wrong totals.
# Fix the logic, then replace prints with proper tests.
# ---------------------------------------------------------------------------


def calculate_gst(amount: float, rate: float = 0.18) -> float:
    """Return GST amount on a taxable value."""
    return round(amount * rate, 2)


def simple_interest(principal: float, rate_percent: float, years: float) -> float:
    """SI = P * R * T / 100"""
    return round(principal * rate_percent * years / 100, 2)


def invoice_total_debug_demo(line_items: list[dict]) -> float:
    """Demo function showing print-debug tip (remove prints in production)."""
    running = 0.0
    for i, item in enumerate(line_items):
        subtotal = item["qty"] * item["price"]
        gst = calculate_gst(subtotal, item.get("gst_rate", 0.18))
        line_total = subtotal + gst
        # DEBUG TIP: uncomment next line to see each step
        # print(f"  Line {i+1}: sub={subtotal}, gst={gst}, total={line_total}")
        running += line_total
    return round(running, 2)


# LIVE DEMOS — assert-based quick checks
def demo_assert_tests() -> None:
    print("LIVE DEMO — assert checks on GST")
    assert calculate_gst(1000) == 180.0, "18% of 1000 should be 180"
    assert calculate_gst(500, 0.05) == 25.0, "5% of 500 should be 25"
    assert calculate_gst(0) == 0.0, "GST on zero should be zero"
    print("  All assert checks passed.")


class TestSimpleInterest(unittest.TestCase):
    """unittest for simple_interest function."""

    def test_one_year(self) -> None:
        self.assertEqual(simple_interest(10000, 8, 1), 800.0)

    def test_two_years(self) -> None:
        self.assertEqual(simple_interest(10000, 8, 2), 1600.0)

    def test_zero_principal(self) -> None:
        self.assertEqual(simple_interest(0, 8, 5), 0.0)


def demo_print_debug() -> None:
    print("\nLIVE DEMO — print-debug on invoice lines")
    items = [
        {"qty": 2, "price": 500, "gst_rate": 0.18},
        {"qty": 1, "price": 1200, "gst_rate": 0.12},
    ]
    total = invoice_total_debug_demo(items)
    print(f"  Invoice grand total: Rs. {total:,.2f}")
    print("  Tip: add print() inside the loop to inspect each line.")


def main() -> None:
    demo_assert_tests()
    demo_print_debug()

    print("\nLIVE DEMO — unittest.TestCase")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSimpleInterest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("  unittest suite: all tests passed.")
    else:
        print("  unittest suite: some tests failed.")

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Add an assert that calculate_gst(250, 0.12) equals 30.0.
    # 2) Add a unittest method test_half_year for SI over 0.5 years.
    #
    # Solution 1:
    #   assert calculate_gst(250, 0.12) == 30.0
    #
    # Solution 2:
    #   def test_half_year(self):
    #       self.assertEqual(simple_interest(10000, 8, 0.5), 400.0)
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Write a TestCase for calculate_gst with at least 3 edge cases
    # (zero amount, 5% rate, rounding).


if __name__ == "__main__":
    main()
