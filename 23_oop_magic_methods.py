"""
Lesson 23: OOP — Magic Methods (Dunder Methods)
===============================================
Special methods like __str__, __repr__, __eq__, __add__ make objects
print nicely, compare correctly, and combine in intuitive ways.

Run: python 23_oop_magic_methods.py
"""

# =============================================================================
# CONCEPT
# =============================================================================
# Magic methods have double underscores: __name__
#
#   __str__   — human-friendly string (print(obj))
#   __repr__  — developer-friendly, ideally valid Python to recreate obj
#   __eq__    — equality (obj1 == obj2)
#   __add__   — addition (obj1 + obj2)
#
# Commerce use:
#   Money(100) + Money(50)  →  Money(150)
#   InvoiceLine items compared by SKU and amount

print("=" * 60)
print("LESSON 23: OOP — Magic Methods")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

class Money:
    """Represents an amount in Indian Rupees."""

    def __init__(self, amount, currency="INR"):
        self.amount = round(float(amount), 2)
        self.currency = currency

    def __str__(self):
        return f"Rs {self.amount:,.2f}"

    def __repr__(self):
        return f"Money({self.amount}, currency='{self.currency}')"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)


class InvoiceLine:
    """One line on a tax invoice."""

    def __init__(self, sku, description, qty, unit_price, gst_rate=0.18):
        self.sku = sku
        self.description = description
        self.qty = qty
        self.unit_price = unit_price
        self.gst_rate = gst_rate

    @property
    def subtotal(self):
        return round(self.qty * self.unit_price, 2)

    @property
    def gst_amount(self):
        return round(self.subtotal * self.gst_rate, 2)

    @property
    def line_total(self):
        return round(self.subtotal + self.gst_amount, 2)

    def __str__(self):
        return (
            f"{self.description} x{self.qty} @ Rs {self.unit_price:,.2f} "
            f"= Rs {self.line_total:,.2f} (incl. GST)"
        )

    def __repr__(self):
        return (
            f"InvoiceLine('{self.sku}', '{self.description}', "
            f"{self.qty}, {self.unit_price}, gst_rate={self.gst_rate})"
        )

    def __eq__(self, other):
        if not isinstance(other, InvoiceLine):
            return NotImplemented
        return (
            self.sku == other.sku
            and self.qty == other.qty
            and self.unit_price == other.unit_price
        )

    def __add__(self, other):
        if not isinstance(other, InvoiceLine):
            return NotImplemented
        if self.sku != other.sku or self.unit_price != other.unit_price:
            raise ValueError("Can only merge identical SKU/price lines")
        return InvoiceLine(
            self.sku,
            self.description,
            self.qty + other.qty,
            self.unit_price,
            self.gst_rate,
        )


# --- Demo: Money ---
print("\n--- Money Demo ---")
payment = Money(12500)
tax = Money(2250)
total = payment + tax
print(f"Payment: {payment}")           # uses __str__
print(f"Tax:     {tax}")
print(f"Total:   {total}")
print(f"repr:    {repr(total)}")       # uses __repr__
print(f"Equal?   {payment == Money(12500)}")

gst_on_bill = Money(1800) * 1.18  # scale via __mul__
print(f"Scaled:  {gst_on_bill}")

# --- Demo: InvoiceLine ---
print("\n--- InvoiceLine Demo ---")
line1 = InvoiceLine("SKU-PEN", "Pen Box", 5, 80.0, gst_rate=0.12)
line2 = InvoiceLine("SKU-PEN", "Pen Box", 3, 80.0, gst_rate=0.12)
line3 = InvoiceLine("SKU-CALC", "Calculator", 2, 450.0, gst_rate=0.18)

print(line1)
print(line2)
merged = line1 + line2
print(f"Merged pens: {merged}")
print(f"Same line twice? {line1 == line2}")

invoice_total = Money(line3.line_total) + Money(merged.line_total)
print(f"Invoice subtotal (2 lines): {invoice_total}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Create Money(5000) and Money(1200). Add them. Print result.

# a = Money(5000)
# b = Money(1200)
# print(a + b)

# Exercise 2: Two InvoiceLines same SKU — merge with +. Print qty and total.

# l1 = InvoiceLine("SKU-A4", "A4 Paper", 10, 250.0, gst_rate=0.12)
# l2 = InvoiceLine("SKU-A4", "A4 Paper", 5, 250.0, gst_rate=0.12)
# combined = l1 + l2
# print(f"Qty: {combined.qty}, Total: Rs {combined.line_total:,.2f}")

# Exercise 3: Check equality of Money(99.99) and Money(100) — should be False.

# print(Money(99.99) == Money(100))


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
Build a 3-line invoice using InvoiceLine objects:
  - Merge any duplicate SKUs with +
  - Sum all line totals using Money + Money
  - Print each line with print(line) and final grand total
""")

# --- Mini challenge reference solution ---
raw_lines = [
    InvoiceLine("SKU-LED", "Ledger Book", 4, 120.0, gst_rate=0.12),
    InvoiceLine("SKU-LED", "Ledger Book", 6, 120.0, gst_rate=0.12),
    InvoiceLine("SKU-USB", "USB Drive", 2, 299.0, gst_rate=0.18),
]

merged_led = raw_lines[0] + raw_lines[1]
final_lines = [merged_led, raw_lines[2]]

grand = Money(0)
print("\nChallenge result:")
for line in final_lines:
    print(f"  {line}")
    grand = grand + Money(line.line_total)
print(f"  GRAND TOTAL: {grand}")

print("\nLesson 23 complete.")
