"""
Lesson 03: Numbers and Math Operators
Learning goals: Use +, -, *, /, //, %, **, and round() for commerce calculations:
                GST, discounts, simple interest, profit/loss.
Why commerce cares: Wrong math on an invoice or loan statement costs money and trust.
                    Python handles decimals and rounding consistently.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# ARITHMETIC OPERATORS:
#   +   addition          total = price + gst
#   -   subtraction       profit = selling - cost
#   *   multiplication    amount = rate * quantity
#   /   division          per_unit = total / qty        (always gives float)
#   //  floor division    full_boxes = items // 12      (whole number part)
#   %   modulo (remainder) change = paid % bill_amount  (also: is_even = n % 2)
#   **  exponent          compound = principal * (1 + r/100) ** years
#
# round(value, decimals) — round for display (GST often rounded to 2 decimal places)
#
# COMMERCE FORMULAS:
#   GST amount     = taxable_value * (gst_rate / 100)
#   Discount amount = price * (discount_percent / 100)
#   Simple Interest = P * R * T / 100   (P=principal, R=rate%, T=time in years)
#   Profit         = Revenue - Cost
#   Profit %       = (Profit / Cost) * 100

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("NUMBERS & MATH — COMMERCE CALCULATIONS")
print("=" * 50)

# --- Demo 1: GST calculation ---
taxable_value = 10000.00
cgst_rate = 9.0    # Central GST 9%
sgst_rate = 9.0    # State GST 9%
# Total GST = 18% split as CGST + SGST (intra-state supply)

cgst = round(taxable_value * (cgst_rate / 100), 2)
sgst = round(taxable_value * (sgst_rate / 100), 2)
total_gst = cgst + sgst
invoice_total = taxable_value + total_gst

print("\n--- GST Breakdown (Intra-state) ---")
print(f"Taxable Value : Rs. {taxable_value:,.2f}")
print(f"CGST @ {cgst_rate}%    : Rs. {cgst}")
print(f"SGST @ {sgst_rate}%    : Rs. {sgst}")
print(f"Total GST     : Rs. {total_gst}")
print(f"Invoice Total : Rs. {invoice_total:,.2f}")

# --- Demo 2: Trade discount + cash discount ---
list_price = 25000
trade_discount_pct = 10   # discount to retailer
price_after_trade = list_price - list_price * (trade_discount_pct / 100)
cash_discount_pct = 2     # extra 2% if paid within 7 days
cash_discount = price_after_trade * (cash_discount_pct / 100)
final_price = price_after_trade - cash_discount

print("\n--- Discount Stack ---")
print(f"List Price       : Rs. {list_price:,.2f}")
print(f"After {trade_discount_pct}% trade disc : Rs. {price_after_trade:,.2f}")
print(f"Cash discount 2% : Rs. {cash_discount:,.2f}")
print(f"Final Price      : Rs. {final_price:,.2f}")

# --- Demo 3: Simple interest (FD / loan style) ---
principal = 100000        # Rs. 1 lakh fixed deposit
annual_rate = 7.5         # 7.5% per annum
time_years = 2

simple_interest = principal * annual_rate * time_years / 100
maturity_amount = principal + simple_interest

print("\n--- Simple Interest (Bank FD) ---")
print(f"Principal  : Rs. {principal:,.2f}")
print(f"Rate       : {annual_rate}% p.a.")
print(f"Time       : {time_years} years")
print(f"Interest   : Rs. {simple_interest:,.2f}")
print(f"Maturity   : Rs. {maturity_amount:,.2f}")

# --- Demo 4: Profit and loss ---
cost_price = 45000
selling_price = 52000
profit = selling_price - cost_price
profit_percent = (profit / cost_price) * 100

print("\n--- Profit / Loss ---")
if profit >= 0:
    print(f"Profit: Rs. {profit:,.2f} ({profit_percent:.1f}% on cost)")
else:
    loss = abs(profit)
    print(f"Loss: Rs. {loss:,.2f}")

# --- Demo 5: // and % — packing & change ---
total_units = 145
units_per_carton = 12
full_cartons = total_units // units_per_carton
loose_units = total_units % units_per_carton

print("\n--- Inventory Packing ---")
print(f"Total units: {total_units}")
print(f"Full cartons ({units_per_carton}/box): {full_cartons}")
print(f"Loose units remaining: {loose_units}")

bill_amount = 847.50
amount_paid = 1000
change = amount_paid - bill_amount
print(f"\nBill: Rs. {bill_amount}, Paid: Rs. {amount_paid}, Change: Rs. {change:.2f}")

# --- Demo 6: ** for compound growth sketch ---
revenue_year1 = 500000
growth_rate = 0.15   # 15% annual growth
revenue_year3 = revenue_year1 * (1 + growth_rate) ** 2   # year 3 from year 1

print("\n--- Revenue Projection (15% growth) ---")
print(f"Year 1 Revenue : Rs. {revenue_year1:,.0f}")
print(f"Year 3 Revenue : Rs. {revenue_year3:,.0f}")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Base Rs. 2400, GST 5%. Print gst_amount and total (round to 2 decimals).
# Exercise 2: MRP Rs. 999, discount 25%. Print sale price.
# Exercise 3: P=50000, R=8%, T=3 years. Print simple interest and amount.

# --- Student code area ---
# base = 2400
# gst = round(base * 0.05, 2)
# print(gst, base + gst)

# --- Solutions ---
# mrp = 999
# sale = mrp - mrp * 0.25
# print(f"Sale price: Rs. {sale}")
# p, r, t = 50000, 8, 3
# si = p * r * t / 100
# print(f"SI: Rs. {si}, Amount: Rs. {p + si}")

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# A wholesaler sells rice:
#   50 bags at Rs. 1200/bag, 5% trade discount, 18% GST on discounted value.
# Calculate: gross, discount, taxable value, GST, net invoice amount.

print("\n--- MINI CHALLENGE: Rice Wholesale Invoice ---")
bags = 50
rate_per_bag = 1200
trade_disc = 5
gst_pct = 18

gross = bags * rate_per_bag
disc_amt = gross * (trade_disc / 100)
taxable = gross - disc_amt
gst_amt = round(taxable * (gst_pct / 100), 2)
net = taxable + gst_amt

print(f"Gross ({bags} bags)  : Rs. {gross:,.2f}")
print(f"Trade discount {trade_disc}% : Rs. {disc_amt:,.2f}")
print(f"Taxable value        : Rs. {taxable:,.2f}")
print(f"GST @ {gst_pct}%            : Rs. {gst_amt:,.2f}")
print(f"NET PAYABLE          : Rs. {net:,.2f}")
