"""
Lesson 12: While Loops
======================
Goals:
  - Repeat code while a condition stays True.
  - Build menu-driven logic (ATM-style) without blocking on keyboard input.
  - Model compound interest year by year.

Why commerce cares:
  Banking apps, billing kiosks, and interest calculators often loop until
  the user exits or a financial goal is reached. while fits "keep going until…"
"""

USE_INPUT = False

# ---------------------------------------------------------------------------
# CONCEPT: while condition:
# ---------------------------------------------------------------------------
# The condition is checked BEFORE each iteration.
# Always ensure something inside the loop moves toward exit (counter, flag, input).
# Infinite loops hang the program — dangerous in production scripts.

print("=" * 60)
print("LESSON 12 — WHILE LOOPS")
print("=" * 60)

# ---------------------------------------------------------------------------
# LIVE DEMO 1 — ATM-style menu with simulated choices (no blocking input)
# ---------------------------------------------------------------------------
print("\n--- DEMO 1: ATM menu (simulated choices) ---")

balance = 25000.0
# Simulated user taps: 1=balance, 2=withdraw, 3=deposit, 4=exit
simulated_choices = ["1", "2", "2", "3", "1", "4"]
choice_index = 0

print(f"Opening balance: Rs {balance:,.2f}")
print("Menu: 1=Balance  2=Withdraw  3=Deposit  4=Exit")

while True:
    if choice_index < len(simulated_choices):
        choice = simulated_choices[choice_index]
        choice_index += 1
        print(f"\n>> Simulated choice: {choice}")
    elif USE_INPUT:
        choice = input("Enter choice (1-4): ").strip()
    else:
        choice = "4"  # auto-exit if demo list exhausted

    if choice == "1":
        print(f"  Available balance: Rs {balance:,.2f}")
    elif choice == "2":
        withdraw = 5000  # demo amount
        if withdraw > balance:
            print("  Insufficient funds.")
        else:
            balance -= withdraw
            print(f"  Withdrew Rs {withdraw:,.2f}. New balance: Rs {balance:,.2f}")
    elif choice == "3":
        deposit = 2000  # demo amount
        balance += deposit
        print(f"  Deposited Rs {deposit:,.2f}. New balance: Rs {balance:,.2f}")
    elif choice == "4":
        print("  Thank you. Session ended.")
        break
    else:
        print("  Invalid option — try again.")

# ---------------------------------------------------------------------------
# LIVE DEMO 2 — Compound interest: year-by-year growth
# ---------------------------------------------------------------------------
print("\n--- DEMO 2: Compound interest (while years < term) ---")

principal = 100000  # fixed deposit
annual_rate = 0.075  # 7.5% p.a.
years = 0
term_years = 5

amount = principal
print(f"{'Year':>4} {'Opening':>12} {'Interest':>12} {'Closing':>12}")
print("-" * 44)

while years < term_years:
    opening = amount
    interest = round(opening * annual_rate, 2)
    amount = round(opening + interest, 2)
    years += 1
    print(f"{years:>4} {opening:>12,.2f} {interest:>12,.2f} {amount:>12,.2f}")

print(f"\nRs {principal:,} grows to Rs {amount:,.2f} in {term_years} years.")

# ---------------------------------------------------------------------------
# LIVE DEMO 3 — Countdown: days until payment due
# ---------------------------------------------------------------------------
print("\n--- DEMO 3: Days until invoice due ---")

days_left = 7
invoice_ref = "INV-1008"

while days_left > 0:
    print(f"  {invoice_ref}: {days_left} day(s) remaining for payment.")
    days_left -= 1
print(f"  {invoice_ref}: DUE TODAY — send payment reminder.")

# ---------------------------------------------------------------------------
# LIVE DEMO 4 — Validate PIN attempts (max 3 tries)
# ---------------------------------------------------------------------------
print("\n--- DEMO 4: PIN retry limit ---")

correct_pin = "4829"
attempt_pins = ["0000", "1234", "4829"]  # simulated attempts
attempt = 0
max_attempts = 3
unlocked = False

while attempt < max_attempts and not unlocked:
    pin = attempt_pins[attempt] if attempt < len(attempt_pins) else correct_pin
    attempt += 1
    print(f"  Attempt {attempt}: entered {pin}")
    if pin == correct_pin:
        unlocked = True
        print("  Access granted.")
    elif attempt < max_attempts:
        print("  Wrong PIN — try again.")
    else:
        print("  Card blocked — too many attempts.")

# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
print("\n--- EXERCISES ---")
print("1. Use while to double a value starting at 1000 until it exceeds 50000.")
print("2. Simulate reducing loan balance by Rs 5000 per month until balance <= 0.")
print("3. Print 'Processing batch N' for N = 1 to 5 using a while loop.")

# Solution 1:
# val = 1000
# while val <= 50000:
#     print(val)
#     val *= 2

# Solution 2:
# loan = 35000
# month = 0
# while loan > 0:
#     month += 1
#     loan -= 5000
#     print(f"Month {month}: balance Rs {max(loan, 0)}")

# Solution 3:
# n = 1
# while n <= 5:
#     print(f"Processing batch {n}")
#     n += 1

# ---------------------------------------------------------------------------
# MINI CHALLENGE
# ---------------------------------------------------------------------------
print("\n--- MINI CHALLENGE ---")
print(
    "A shop targets Rs 1,00,000 monthly sales. Daily sales are "
    "[12000, 8500, 15000, 9200, 18000, 11000]. "
    "Use while to add days until cumulative sales >= target; print day count."
)

daily = [12000, 8500, 15000, 9200, 18000, 11000]
target = 100000
idx = 0
cumulative = 0
while cumulative < target and idx < len(daily):
    cumulative += daily[idx]
    idx += 1
    print(f"  After day {idx}: Rs {cumulative:,}")
print(f"Target reached in {idx} day(s).")

if USE_INPUT:
    feedback = input("Rate this lesson 1-5: ")
    print(f"Thanks for rating: {feedback}")

print("\nLesson 12 complete.")
