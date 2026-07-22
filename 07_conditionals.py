"""
Lesson 07: Conditionals (if / elif / else)
Learning goals: Branch logic with if/elif/else for profit vs loss, GST slab sketch,
                and loan eligibility decisions.
Why commerce cares: Every business decision is conditional — pricing tiers, tax slabs,
                    approval workflows, and late-fee rules all use if/else logic.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# if condition:
#     # run when condition is True
# elif other_condition:
#     # run when first was False and this is True
# else:
#     # run when all above were False
#
# INDENTATION matters — Python uses spaces (usually 4) to show which lines belong
# to which branch.
#
# COMMERCE PATTERNS:
#   if revenue > cost: profit else: loss
#   if turnover < threshold: no GST else: register
#   if score >= 750: rate = 8.5% elif score >= 650: rate = 10.5% else: reject

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("CONDITIONALS — PROFIT, GST SLABS, LOAN ELIGIBILITY")
print("=" * 50)

# --- Demo 1: Profit vs Loss ---
cost_price = 42000
selling_price = 38500

print("\n--- Profit / Loss Statement ---")
print(f"Cost    : Rs. {cost_price:,.2f}")
print(f"Selling : Rs. {selling_price:,.2f}")

if selling_price > cost_price:
    profit = selling_price - cost_price
    margin = (profit / cost_price) * 100
    print(f"Result  : PROFIT of Rs. {profit:,.2f} ({margin:.1f}% margin)")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Result  : LOSS of Rs. {loss:,.2f}")
else:
    print("Result  : BREAK-EVEN (no profit, no loss)")

# --- Demo 2: GST rate by product category (simplified) ---
product_category = "packaged_food"
taxable_value = 500.00

print("\n--- GST Rate by Category ---")
if product_category == "essential_food":
    gst_rate = 0
elif product_category == "packaged_food":
    gst_rate = 5
elif product_category == "standard_goods":
    gst_rate = 12
elif product_category == "luxury_services":
    gst_rate = 18
else:
    gst_rate = 18   # default

gst_amount = taxable_value * (gst_rate / 100)
print(f"Category '{product_category}' -> GST {gst_rate}%")
print(f"Taxable Rs. {taxable_value:.2f} + GST Rs. {gst_amount:.2f} = Rs. {taxable_value + gst_amount:.2f}")

# --- Demo 3: Income tax slab sketch (Old regime simplified education demo) ---
taxable_income = 725000

print("\n--- Income Tax Slab Sketch (Educational) ---")
if taxable_income <= 250000:
    tax = 0
    slab_label = "Up to 2.5L — Nil"
elif taxable_income <= 500000:
    tax = (taxable_income - 250000) * 0.05
    slab_label = "2.5L–5L @ 5%"
elif taxable_income <= 1000000:
    tax = 12500 + (taxable_income - 500000) * 0.20
    slab_label = "5L–10L @ 20% (with lower slab)"
else:
    tax = 112500 + (taxable_income - 1000000) * 0.30
    slab_label = "Above 10L @ 30%"

print(f"Taxable income : Rs. {taxable_income:,}")
print(f"Slab applied   : {slab_label}")
print(f"Tax (approx)   : Rs. {tax:,.2f}")

# --- Demo 4: Loan eligibility ---
annual_income = 550000
existing_emi = 12000
requested_loan = 800000
credit_score = 720
employment_years = 2

print("\n--- Home Loan Eligibility ---")
print(f"Income: Rs. {annual_income:,}/yr | EMI: Rs. {existing_emi:,}/mo | Score: {credit_score}")

monthly_income = annual_income / 12
max_emi_allowed = monthly_income * 0.5   # 50% FOIR rule (simplified)
estimated_emi = requested_loan * 0.010   # rough 1% of principal as EMI demo
total_emi = existing_emi + estimated_emi

if credit_score < 650:
    decision = "REJECTED"
    reason = "Credit score below 650"
elif employment_years < 1:
    decision = "REJECTED"
    reason = "Insufficient employment history"
elif total_emi > max_emi_allowed:
    decision = "REJECTED"
    reason = f"EMI burden Rs. {total_emi:,.0f} exceeds 50% of income"
elif requested_loan > annual_income * 5:
    decision = "REJECTED"
    reason = "Loan amount exceeds 5x annual income"
else:
    decision = "APPROVED"
    reason = "All criteria met"

print(f"Max EMI allowed: Rs. {max_emi_allowed:,.0f}")
print(f"Estimated EMI  : Rs. {estimated_emi:,.0f}")
print(f"DECISION: {decision} — {reason}")

# --- Demo 5: Early payment discount ---
invoice_amount = 50000
days_to_pay = 5
payment_terms_days = 30

print("\n--- Early Payment Discount ---")
if days_to_pay <= 7:
    discount_pct = 2
elif days_to_pay <= 15:
    discount_pct = 1
else:
    discount_pct = 0

discount = invoice_amount * (discount_pct / 100)
net_payable = invoice_amount - discount
print(f"Invoice: Rs. {invoice_amount:,.2f}, Paid on day {days_to_pay}")
print(f"Discount: {discount_pct}% = Rs. {discount:,.2f}")
print(f"Net paid: Rs. {net_payable:,.2f}")

# --- Demo 6: Nested if — stock alert ---
stock_qty = 8
reorder_level = 15
is_fast_moving = True

print("\n--- Inventory Alert ---")
if stock_qty <= reorder_level:
    if stock_qty == 0:
        print("CRITICAL: Out of stock — stop sales!")
    elif is_fast_moving:
        print(f"URGENT: Only {stock_qty} units left (fast-moving item)")
    else:
        print(f"LOW STOCK: {stock_qty} units — reorder soon")
else:
    print(f"Stock OK: {stock_qty} units on hand")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: If bill >= 5000, delivery free; else charge Rs. 80. bill=3200.
# Exercise 2: Classify turnover: <40L small, 40L-1.5Cr medium, else large. turnover=95L.
# Exercise 3: If payment_mode is "cash" and amount > 200000, flag "PAN required".

# --- Student code area ---
# bill = 3200
# if bill >= 5000:
#     delivery = 0
# else:
#     delivery = 80
# print(delivery)

# --- Solutions ---
# turnover = 9500000
# if turnover < 4000000:
#     size = "small"
# elif turnover < 15000000:
#     size = "medium"
# else:
#     size = "large"
# print(size)

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# GST filing reminder: days_left to file. if <0: overdue+penalty, elif <=3: urgent,
# elif <=10: reminder, else: on track. Use demo days_left = 2.

print("\n--- MINI CHALLENGE: GST Filing Status ---")
days_left = 2
filing_month = "June 2026"

if days_left < 0:
    status = "OVERDUE"
    action = f"File immediately — late fee may apply ({abs(days_left)} days late)"
elif days_left <= 3:
    status = "URGENT"
    action = f"File within {days_left} days for {filing_month}"
elif days_left <= 10:
    status = "REMINDER"
    action = f"GSTR-1 for {filing_month} due in {days_left} days"
else:
    status = "ON TRACK"
    action = f"No immediate action — {days_left} days remaining"

print(f"Status : {status}")
print(f"Action : {action}")
