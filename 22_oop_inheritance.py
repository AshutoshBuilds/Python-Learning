"""
Lesson 22: OOP — Inheritance
============================
Child classes reuse parent behaviour and add specialised rules.
Savings vs Current accounts: different minimum balance and overdraft rules.

Run: python 22_oop_inheritance.py
"""

# =============================================================================
# CONCEPT
# =============================================================================
# INHERITANCE lets a child class extend a parent class.
#
#   class Child(Parent):
#       def __init__(self, ...):
#           super().__init__(...)   # call parent constructor
#
# Override methods to change behaviour (e.g. withdraw rules).
#
# Commerce analogy:
#   BankAccount (base)     — common deposit/withdraw
#   SavingsAccount         — higher min balance, no overdraft
#   CurrentAccount         — lower min balance, allows overdraft up to a limit

print("=" * 60)
print("LESSON 22: OOP — Inheritance")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

class BankAccount:
    """Base bank account with standard deposit and withdraw."""

    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def account_type(self):
        return "Generic"


class SavingsAccount(BankAccount):
    """Savings: must keep minimum balance; no overdraft."""

    MIN_BALANCE = 1000.0

    def __init__(self, account_number, holder_name, balance=0.0):
        super().__init__(account_number, holder_name, balance)
        if self.balance < self.MIN_BALANCE:
            raise ValueError(
                f"Savings account needs min Rs {self.MIN_BALANCE:,.2f} opening balance"
            )

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(
                f"Cannot go below min balance Rs {self.MIN_BALANCE:,.2f}"
            )
        self.balance -= amount
        return self.balance

    def account_type(self):
        return "Savings"


class CurrentAccount(BankAccount):
    """Current: lower min balance; overdraft facility allowed."""

    MIN_BALANCE = 500.0

    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=10000.0):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        lowest_allowed = -self.overdraft_limit
        if self.balance - amount < lowest_allowed:
            raise ValueError(
                f"Exceeds overdraft limit of Rs {self.overdraft_limit:,.2f}"
            )
        self.balance -= amount
        return self.balance

    def account_type(self):
        return "Current"

    def available_funds(self):
        return self.balance + self.overdraft_limit


def print_account_summary(account):
    print(
        f"  {account.account_type()} | {account.account_number} | "
        f"{account.holder_name} | Balance: Rs {account.balance:,.2f}"
    )


# --- Demo: SavingsAccount ---
print("\n--- Savings Account ---")
savings = SavingsAccount("SAV-001", "Sharma Traders", balance=5000)
print_account_summary(savings)
savings.withdraw(3500)
print(f"  After withdraw Rs 3,500: Rs {savings.balance:,.2f}")

try:
    savings.withdraw(1000)  # would drop below min 1000
except ValueError as err:
    print(f"  Blocked: {err}")

# --- Demo: CurrentAccount with overdraft ---
print("\n--- Current Account (overdraft) ---")
current = CurrentAccount("CUR-001", "Mehta Bank Supplies", balance=2000, overdraft_limit=15000)
print_account_summary(current)
print(f"  Available funds (incl. OD): Rs {current.available_funds():,.2f}")
current.withdraw(12000)
print(f"  After withdraw Rs 12,000: Rs {current.balance:,.2f}")

try:
    current.withdraw(10000)  # exceeds overdraft
except ValueError as err:
    print(f"  Blocked: {err}")

# --- Demo: polymorphism — same interface, different rules ---
print("\n--- Polymorphism: list of accounts ---")
accounts = [
    SavingsAccount("SAV-002", "Patel Retail", balance=3000),
    CurrentAccount("CUR-002", "Gupta & Co", balance=1000, overdraft_limit=20000),
]
for acct in accounts:
    acct.deposit(500)
    print_account_summary(acct)


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Open SavingsAccount with Rs 2000. Withdraw Rs 500.
# Print balance.

# sav = SavingsAccount("SAV-EX", "Exercise Co", balance=2000)
# sav.withdraw(500)
# print(f"Balance: Rs {sav.balance:,.2f}")

# Exercise 2: Open CurrentAccount balance Rs 0, overdraft Rs 5000.
# Withdraw Rs 3000 (goes negative). Print balance.

# cur = CurrentAccount("CUR-EX", "Exercise Co", balance=0, overdraft_limit=5000)
# cur.withdraw(3000)
# print(f"Balance: Rs {cur.balance:,.2f}")

# Exercise 3: Use isinstance() to check if an account is SavingsAccount.

# acct = SavingsAccount("SAV-CHK", "Test", balance=1500)
# print(isinstance(acct, SavingsAccount))  # True
# print(isinstance(acct, BankAccount))     # True — savings IS-A bank account


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
A business receives Rs 25,000 and splits banking:
  - Rs 15,000 -> Savings (emergency fund)
  - Rs 10,000 -> Current (daily expenses)

Simulate:
  1. Create both accounts with those opening balances.
  2. Pay salary Rs 8,000 from Current.
  3. Pay vendor Rs 2,000 from Savings.
  4. Print both balances and total cash position (sum of balances;
     Current may be negative if overdraft used — here it should not be).
""")

# --- Mini challenge reference solution ---
biz_savings = SavingsAccount("SAV-BIZ", "Gupta & Co", balance=15000)
biz_current = CurrentAccount("CUR-BIZ", "Gupta & Co", balance=10000, overdraft_limit=25000)

biz_current.withdraw(8000)
biz_savings.withdraw(2000)

total_position = biz_savings.balance + biz_current.balance
print(f"\nChallenge result:")
print(f"  Savings balance:  Rs {biz_savings.balance:,.2f}")
print(f"  Current balance:  Rs {biz_current.balance:,.2f}")
print(f"  Total position:   Rs {total_position:,.2f}")

print("\nLesson 22 complete.")
