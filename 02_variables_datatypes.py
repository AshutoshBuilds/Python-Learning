"""
Lesson 02: Variables and Data Types
Learning goals: Create variables, use int/float/str/bool, check types with type(),
                follow naming rules, and store commerce data (balance, GST rate, shop name).
Why commerce cares: Every invoice field — amount, customer name, tax rate, paid/unpaid flag —
                    is stored in a variable with a specific data type.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# A VARIABLE is a labelled box that holds a value.
#   bank_balance = 50000   →  box named "bank_balance" holds 50000
#
# DATA TYPES (what kind of value is in the box):
#   int   — whole numbers        e.g.  quantity = 12, gst_rate = 18
#   float — decimal numbers      e.g.  price = 499.99, interest = 7.5
#   str   — text (in quotes)     e.g.  shop_name = "Patel Electronics"
#   bool  — True or False        e.g.  is_paid = True, credit_exceeded = False
#
# type(variable) tells you the data type — useful when debugging calculations.
#
# NAMING RULES:
#   - Use lowercase_with_underscores (snake_case): total_amount, gst_rate
#   - Start with a letter, not a number
#   - No spaces; use _ instead
#   - Names should describe the business meaning: invoice_date, not x

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("VARIABLES & DATA TYPES — COMMERCE EXAMPLES")
print("=" * 50)

# --- Demo 1: Bank account variables ---
account_holder = "Riya Mehta"          # str
account_number = "SB-00452189"         # str (account numbers are text, not math!)
opening_balance = 75000                # int
interest_earned = 1250.75              # float
is_active = True                       # bool

print("\n--- Bank Account Record ---")
print(f"Holder   : {account_holder}  (type: {type(account_holder).__name__})")
print(f"Account  : {account_number}  (type: {type(account_number).__name__})")
print(f"Balance  : Rs. {opening_balance:,}  (type: {type(opening_balance).__name__})")
print(f"Interest : Rs. {interest_earned}  (type: {type(interest_earned).__name__})")
print(f"Active?  : {is_active}  (type: {type(is_active).__name__})")

closing_balance = opening_balance + interest_earned
print(f"Closing  : Rs. {closing_balance:,.2f}")

# --- Demo 2: GST and shop details ---
shop_name = "Kumar & Sons Traders"
gstin = "27AABCU9603R1ZM"               # 15-character GST Identification Number
state_code = 27                        # Maharashtra
default_gst_rate = 18.0                # float for percentage
is_composition_scheme = False          # small business scheme — no GST collection

print("\n--- Shop & Tax Setup ---")
print(f"Shop Name    : {shop_name}")
print(f"GSTIN        : {gstin}")
print(f"State Code   : {state_code}")
print(f"Default GST% : {default_gst_rate}%")
print(f"Composition? : {is_composition_scheme}")

# --- Demo 3: Mixing types carefully ---
unit_price = 1250          # int
quantity = 3                 # int
discount_percent = 5.5       # float

subtotal = unit_price * quantity                    # int * int = int
discount_amount = subtotal * (discount_percent / 100)  # becomes float
net_before_tax = subtotal - discount_amount

print("\n--- Order Calculation ---")
print(f"Unit Price  : Rs. {unit_price} ({type(unit_price).__name__})")
print(f"Quantity    : {quantity}")
print(f"Subtotal    : Rs. {subtotal}")
print(f"Discount 5.5%: Rs. {discount_amount:.2f}")
print(f"Net Amount  : Rs. {net_before_tax:.2f}")

# --- Demo 4: Reassigning variables (balance after transaction) ---
cash_in_hand = 10000
print(f"\nCash before sale: Rs. {cash_in_hand}")
cash_in_hand = cash_in_hand + 2500   # received payment
print(f"Cash after sale : Rs. {cash_in_hand}")
cash_in_hand = cash_in_hand - 800    # paid supplier
print(f"Cash after payment: Rs. {cash_in_hand}")

# --- Demo 5: Boolean flags in business logic ---
invoice_sent = True
payment_received = False
can_close_order = invoice_sent and payment_received
print(f"\nInvoice sent? {invoice_sent}, Payment received? {payment_received}")
print(f"Can close order? {can_close_order}")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Create variables for a product: name (str), price (float), in_stock (bool).
#             Print each with type().
# Exercise 2: Store PAN as str "ABCDE1234F", annual_turnover as int 2500000.
#             Print both.
# Exercise 3: Start with petty_cash = 5000. Add 1200, subtract 350. Print final amount.

# --- Student code area ---
# product_name = "USB Cable"
# product_price = 299.00
# in_stock = True

# --- Solutions ---
# print(f"{product_name}, Rs.{product_price}, stock={in_stock}")
# print(type(product_name), type(product_price), type(in_stock))
# pan = "ABCDE1234F"
# turnover = 2500000
# print(pan, turnover)
# petty_cash = 5000
# petty_cash = petty_cash + 1200 - 350
# print(petty_cash)

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Build a mini "customer credit profile" using variables of all four types:
#   customer_name (str), credit_limit (float), outstanding_dues (float),
#   days_overdue (int), account_blocked (bool)
# Print a formatted summary. Calculate available_credit = credit_limit - outstanding_dues.

print("\n--- MINI CHALLENGE: Credit Profile ---")
customer_name = "Apex Distributors Pvt Ltd"
credit_limit = 500000.00
outstanding_dues = 387500.50
days_overdue = 12
account_blocked = False

available_credit = credit_limit - outstanding_dues

print(f"Customer       : {customer_name}")
print(f"Credit Limit   : Rs. {credit_limit:,.2f}")
print(f"Outstanding    : Rs. {outstanding_dues:,.2f}")
print(f"Available      : Rs. {available_credit:,.2f}")
print(f"Days Overdue   : {days_overdue}")
print(f"Blocked?       : {account_blocked}")
