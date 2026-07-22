"""
Lesson 06: Operators
Learning goals: Comparison (==, !=, <, >, <=, >=), logical (and, or, not),
                and assignment operators; apply to credit limits and tax thresholds.
Why commerce cares: Business rules are comparisons — "Is order above credit limit?",
                    "Is turnover below GST registration threshold?", "Is payment overdue?"
"""

# =============================================================================
# CONCEPT
# =============================================================================
# COMPARISON OPERATORS — return True or False:
#   ==  equal to          gst_rate == 18
#   !=  not equal         status != "CANCELLED"
#   <   less than         balance < 0
#   >   greater than      sales > target
#   <=  less or equal     age <= 60
#   >=  greater or equal  amount >= 20000
#
# LOGICAL OPERATORS — combine conditions:
#   and   both must be True    paid and delivered
#   or    at least one True     cash or card
#   not   reverses True/False   not is_blocked
#
# ASSIGNMENT OPERATORS — update a variable:
#   +=    balance += 1000    same as balance = balance + 1000
#   -=    stock -= 5
#   *=    price *= 1.18      (apply 18% markup)
#   /=    share /= 2
#
# CHAINING: 0 < amount < 100000  (amount is between 0 and 1 lakh)

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("OPERATORS — CREDIT, TAX THRESHOLDS, BUSINESS RULES")
print("=" * 50)

# --- Demo 1: Credit limit check ---
credit_limit = 200000.00
outstanding = 185000.00
new_order_value = 25000.00

total_after_order = outstanding + new_order_value
within_limit = total_after_order <= credit_limit
headroom = credit_limit - outstanding

print("\n--- Credit Limit Check ---")
print(f"Credit Limit    : Rs. {credit_limit:,.2f}")
print(f"Outstanding     : Rs. {outstanding:,.2f}")
print(f"New Order       : Rs. {new_order_value:,.2f}")
print(f"Total if booked : Rs. {total_after_order:,.2f}")
print(f"Within limit?   : {within_limit}")
print(f"Headroom now    : Rs. {headroom:,.2f}")

# --- Demo 2: GST registration threshold (simplified education example) ---
# Businesses above turnover threshold must register for GST (rules vary; demo uses 40 lakh)
annual_turnover = 3850000   # Rs. 38.5 lakh
gst_threshold = 4000000     # Rs. 40 lakh
must_register = annual_turnover >= gst_threshold
near_threshold = annual_turnover >= gst_threshold * 0.9 and not must_register

print("\n--- GST Registration Threshold ---")
print(f"Annual Turnover : Rs. {annual_turnover:,.0f}")
print(f"Threshold       : Rs. {gst_threshold:,.0f}")
print(f"Must register?  : {must_register}")
print(f"Near threshold? : {near_threshold}")

# --- Demo 3: Logical operators — approve a discount ---
order_value = 75000
is_repeat_customer = True
payment_terms = "advance"
is_festival_season = False

# Discount if: (repeat customer AND order >= 50000) OR festival season
eligible_for_discount = (is_repeat_customer and order_value >= 50000) or is_festival_season
# Extra 2% if advance payment
extra_discount = eligible_for_discount and payment_terms == "advance"

print("\n--- Discount Eligibility ---")
print(f"Order value      : Rs. {order_value:,.0f}")
print(f"Repeat customer  : {is_repeat_customer}")
print(f"Payment terms    : {payment_terms}")
print(f"Festival season  : {is_festival_season}")
print(f"Base discount OK : {eligible_for_discount}")
print(f"Extra 2% (advance): {extra_discount}")

# --- Demo 4: Assignment operators on ledger balance ---
cash_balance = 50000.00
print(f"\nCash balance start: Rs. {cash_balance:,.2f}")
cash_balance += 12000.00    # cash sale
print(f"After cash sale   : Rs. {cash_balance:,.2f}")
cash_balance -= 8500.00     # paid rent
print(f"After rent        : Rs. {cash_balance:,.2f}")
cash_balance *= 1.0         # no-op demo; *= used for markups elsewhere
print(f"Final cash        : Rs. {cash_balance:,.2f}")

# --- Demo 5: TDS threshold check ---
# TDS on contractor payment if single payment > 30000 (simplified)
contractor_payment = 45000
tds_rate = 1.0   # 1% demo rate
apply_tds = contractor_payment > 30000
tds_amount = contractor_payment * (tds_rate / 100) if apply_tds else 0
net_payment = contractor_payment - tds_amount

print("\n--- TDS on Contractor Payment ---")
print(f"Gross payment : Rs. {contractor_payment:,.2f}")
print(f"TDS applicable: {apply_tds}")
print(f"TDS @ {tds_rate}%     : Rs. {tds_amount:,.2f}")
print(f"Net payable   : Rs. {net_payment:,.2f}")

# --- Demo 6: not operator — account status ---
account_blocked = False
can_place_order = not account_blocked
print(f"\nAccount blocked: {account_blocked} -> Can place order? {can_place_order}")

# --- Demo 7: Chained comparison — slab check ---
taxable_income = 850000
in_slab = 250000 < taxable_income <= 500000
print(f"Taxable income Rs. {taxable_income:,} in 2.5L–5L slab? {in_slab}")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: limit=100000, used=95000. Print True if used/limit > 0.9 (90% utilized).
# Exercise 2: price=1500, min_bulk=1000, qty=5. Bulk discount if price*qty >= min_bulk.
# Exercise 3: Use += to add three deposits 1000, 2500, 750 to balance starting 0.

# --- Student code area ---
# limit, used = 100000, 95000
# print(used / limit > 0.9)

# --- Solutions ---
# price, min_bulk, qty = 1500, 1000, 5
# print(price * qty >= min_bulk)
# bal = 0
# bal += 1000; bal += 2500; bal += 750
# print(bal)

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# A bank offers a loan only if:
#   (annual_income >= 300000) AND (credit_score >= 700) AND (not has_default)
# Set demo values and print APPROVED or REJECTED with reason flags.

print("\n--- MINI CHALLENGE: Loan Pre-Screen ---")
annual_income = 420000
credit_score = 685
has_default = False

income_ok = annual_income >= 300000
score_ok = credit_score >= 700
default_ok = not has_default
approved = income_ok and score_ok and default_ok

print(f"Income >= 3L?     : {income_ok} (Rs. {annual_income:,})")
print(f"Score >= 700?     : {score_ok} (score: {credit_score})")
print(f"No default?       : {default_ok}")
print(f"DECISION          : {'APPROVED' if approved else 'REJECTED'}")
