"""
Lesson 21: Object-Oriented Programming — Classes & Objects
==========================================================
For commerce students: model real-world entities (products, customers,
bank accounts) using Python classes.

Run: python 21_oop_classes.py
"""

# =============================================================================
# CONCEPT
# =============================================================================
# A CLASS is a blueprint; an OBJECT is one instance built from that blueprint.
#
# Key ideas:
#   __init__(self, ...)  — constructor; runs when you create an object
#   self                 — refers to the current instance
#   Methods              — functions defined inside a class (e.g. deposit)
#
# Commerce analogy:
#   Product   → SKU, price, GST rate
#   Customer  → name, GSTIN, credit limit
#   BankAccount → account number, balance, deposit/withdraw

print("=" * 60)
print("LESSON 21: OOP — Classes & Objects")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

class Product:
    """A product in a retail / wholesale catalogue."""

    def __init__(self, sku, name, unit_price, gst_rate=0.18):
        self.sku = sku
        self.name = name
        self.unit_price = unit_price
        self.gst_rate = gst_rate

    def price_with_gst(self):
        return round(self.unit_price * (1 + self.gst_rate), 2)

    def line_total(self, quantity):
        return round(self.unit_price * quantity * (1 + self.gst_rate), 2)


class Customer:
    """A business customer with a credit limit."""

    def __init__(self, customer_id, name, gstin, credit_limit):
        self.customer_id = customer_id
        self.name = name
        self.gstin = gstin
        self.credit_limit = credit_limit
        self.outstanding = 0.0

    def can_buy_on_credit(self, amount):
        return self.outstanding + amount <= self.credit_limit

    def add_invoice(self, amount):
        if not self.can_buy_on_credit(amount):
            raise ValueError(f"Credit limit exceeded for {self.name}")
        self.outstanding += amount


class BankAccount:
    """Simple savings-style bank account with deposit and withdraw."""

    def __init__(self, account_number, holder_name, opening_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def get_statement_line(self):
        return f"A/C {self.account_number} | {self.holder_name} | Balance: Rs {self.balance:,.2f}"


# --- Demo: Product ---
print("\n--- Product Demo ---")
ledger_book = Product("SKU-001", "Ledger Book", 120.0, gst_rate=0.12)
print(f"Product: {ledger_book.name}")
print(f"Unit price (ex-GST): Rs {ledger_book.unit_price}")
print(f"Price with GST: Rs {ledger_book.price_with_gst()}")
print(f"10 units line total: Rs {ledger_book.line_total(10)}")

# --- Demo: Customer ---
print("\n--- Customer Demo ---")
sharma = Customer("CUST-101", "Sharma Traders", "27AABCS1234F1Z5", credit_limit=50000)
invoice_amount = 12500
if sharma.can_buy_on_credit(invoice_amount):
    sharma.add_invoice(invoice_amount)
    print(f"{sharma.name} invoice Rs {invoice_amount:,.2f} booked.")
    print(f"Outstanding: Rs {sharma.outstanding:,.2f} / Limit: Rs {sharma.credit_limit:,.2f}")

# --- Demo: BankAccount ---
print("\n--- Bank Account Demo ---")
account = BankAccount("ACC-7788", "Mehta Bank Supplies", opening_balance=10000)
print(account.get_statement_line())
account.deposit(5000)
print(f"After deposit Rs 5,000: Rs {account.balance:,.2f}")
account.withdraw(3500)
print(f"After withdraw Rs 3,500: Rs {account.balance:,.2f}")
print(account.get_statement_line())


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Create a Product for "USB Drive" at Rs 299 with 18% GST.
# Print price_with_gst().

# usb = Product("SKU-USB", "USB Drive", 299.0, gst_rate=0.18)
# print(f"USB Drive with GST: Rs {usb.price_with_gst()}")

# Exercise 2: Create Customer "Patel Retail" with credit limit 30000.
# Try adding invoice of 28000 — should succeed. Print outstanding.

# patel = Customer("CUST-202", "Patel Retail", "24AAACP5678G1Z9", 30000)
# patel.add_invoice(28000)
# print(f"Patel outstanding: Rs {patel.outstanding:,.2f}")

# Exercise 3: Open account with Rs 0, deposit 15000, withdraw 4000.
# Print final balance.

# ac = BankAccount("ACC-9900", "Gupta & Co")
# ac.deposit(15000)
# ac.withdraw(4000)
# print(f"Final balance: Rs {ac.balance:,.2f}")


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
Build a mini sales scenario:
  1. Create two Product objects (any stationery items).
  2. Create one Customer with credit limit Rs 10,000.
  3. Calculate total for qty 5 of each product (with GST).
  4. If total fits credit limit, call add_invoice(total).
  5. Print customer outstanding and a one-line bank deposit of the same
     amount into a new BankAccount (simulate payment received).

Example output shape:
  Order total: Rs X
  Outstanding: Rs X
  Bank balance after deposit: Rs X
""")

# --- Mini challenge reference solution (runs automatically) ---
item_a = Product("SKU-PEN", "Pen Box", 80.0, gst_rate=0.12)
item_b = Product("SKU-PAD", "Invoice Pad", 45.0, gst_rate=0.12)
order_total = item_a.line_total(5) + item_b.line_total(5)

buyer = Customer("CUST-MC", "Demo Retail", "27AAAAA0000A1Z5", credit_limit=10000)
if buyer.can_buy_on_credit(order_total):
    buyer.add_invoice(order_total)

collection_account = BankAccount("ACC-COLL", "Demo Retail Collections")
collection_account.deposit(order_total)

print(f"\nChallenge result:")
print(f"  Order total: Rs {order_total:,.2f}")
print(f"  Outstanding: Rs {buyer.outstanding:,.2f}")
print(f"  Bank balance after deposit: Rs {collection_account.balance:,.2f}")

print("\nLesson 21 complete.")
