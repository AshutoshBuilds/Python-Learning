"""
Lesson 08: Lists
Learning goals: Create lists, index, append, slice, and sum() for product prices
                and daily sales data.
Why commerce cares: Sales registers, price lists, and monthly revenue figures are
                    naturally stored as ordered lists — one row per item or per day.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# A LIST is an ordered, changeable collection:  prices = [100, 250, 75]
#
# CREATE:
#   empty = []
#   days = ["Mon", "Tue", "Wed"]
#   amounts = [1200, 3400, 890]
#
# ACCESS:
#   prices[0]     first item
#   prices[-1]    last item
#   prices[1:3]   slice — items at index 1 and 2
#
# MODIFY:
#   prices.append(500)    add to end
#   prices[0] = 110       change item
#   len(prices)           count items
#
# USEFUL FUNCTIONS:
#   sum(prices)           total of numbers
#   min(prices), max(prices)
#   sorted(prices)        new sorted list

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("LISTS — PRICES, SALES, DAILY REVENUE")
print("=" * 50)

# --- Demo 1: Product price list ---
product_names = ["Notebook", "Pen Pack", "Calculator", "File Folder"]
unit_prices = [85, 45, 650, 35]

print("\n--- Product Price List ---")
for i in range(len(product_names)):
    print(f"  {i+1}. {product_names[i]:<15} Rs. {unit_prices[i]:>6}")

print(f"\nMost expensive: {product_names[unit_prices.index(max(unit_prices))]} "
      f"(Rs. {max(unit_prices)})")
print(f"Cheapest      : {product_names[unit_prices.index(min(unit_prices))]} "
      f"(Rs. {min(unit_prices)})")

# --- Demo 2: Shopping cart quantities ---
quantities = [10, 5, 2, 20]
line_totals = []
for i in range(len(unit_prices)):
    line_totals.append(unit_prices[i] * quantities[i])

cart_subtotal = sum(line_totals)
print(f"\n--- Cart Subtotal ---")
for i in range(len(product_names)):
    print(f"  {product_names[i]} x {quantities[i]} = Rs. {line_totals[i]:,}")
print(f"  SUBTOTAL: Rs. {cart_subtotal:,}")

# --- Demo 3: Weekly sales list ---
daily_sales = [12500, 18300, 9800, 22100, 15600, 31200, 8900]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("\n--- Weekly Sales Register ---")
for i in range(len(days)):
    print(f"  {days[i]}: Rs. {daily_sales[i]:>8,}")

week_total = sum(daily_sales)
week_avg = week_total / len(daily_sales)
best_day = days[daily_sales.index(max(daily_sales))]
worst_day = days[daily_sales.index(min(daily_sales))]

print(f"\n  Week Total  : Rs. {week_total:,}")
print(f"  Daily Avg   : Rs. {week_avg:,.0f}")
print(f"  Best day    : {best_day} (Rs. {max(daily_sales):,})")
print(f"  Slowest day : {worst_day} (Rs. {min(daily_sales):,})")

# --- Demo 4: append — new product added to catalogue ---
print("\n--- Adding New Product ---")
product_names.append("Whiteboard")
unit_prices.append(1200)
print(f"Catalogue now has {len(product_names)} items")
print(f"Last item: {product_names[-1]} @ Rs. {unit_prices[-1]}")

# --- Demo 5: Slicing — Q1 vs full year sales (months as list) ---
monthly_revenue = [
    420000, 385000, 510000,   # Q1
    445000, 398000, 522000,   # Q2
    480000, 465000, 550000,   # Q3
    610000, 590000, 720000,   # Q4
]
q1 = monthly_revenue[0:3]
q4 = monthly_revenue[9:12]

print("\n--- Quarterly Revenue Slices ---")
print(f"Q1 (Jan-Mar): Rs. {sum(q1):,}")
print(f"Q4 (Oct-Dec): Rs. {sum(q4):,}")
print(f"Full year    : Rs. {sum(monthly_revenue):,}")

# --- Demo 6: List of invoice amounts — find overdue threshold ---
invoice_amounts = [15000, 8500, 42000, 3200, 67800, 9100]
threshold = 20000
large_invoices = [amt for amt in invoice_amounts if amt >= threshold]

print(f"\n--- Invoices >= Rs. {threshold:,} ---")
print(f"  Amounts: {large_invoices}")
print(f"  Count  : {len(large_invoices)}")
print(f"  Total  : Rs. {sum(large_invoices):,}")

# --- Demo 7: Running total (cumulative sales) ---
print("\n--- Cumulative Weekly Sales ---")
running = 0
for i in range(len(daily_sales)):
    running += daily_sales[i]
    print(f"  Through {days[i]}: Rs. {running:,}")

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Create list gst_rates = [0, 5, 12, 18]. Print rate at index 2.
# Exercise 2: sales = [100, 200, 150]. Append 300. Print sum and len.
# Exercise 3: Slice first 3 elements from [10,20,30,40,50]. Print slice.

# --- Student code area ---
# gst_rates = [0, 5, 12, 18]
# print(gst_rates[2])

# --- Solutions ---
# sales = [100, 200, 150]
# sales.append(300)
# print(sum(sales), len(sales))
# nums = [10, 20, 30, 40, 50]
# print(nums[:3])

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Given 5 product prices, apply 10% discount to each (new list), print old vs new totals.

print("\n--- MINI CHALLENGE: 10% Sale on All Items ---")
original_prices = [999, 1499, 2499, 499, 3299]
discounted_prices = []

for price in original_prices:
    discounted_prices.append(round(price * 0.90, 2))

print(f"{'Product#':<10} {'Original':>12} {'After 10% off':>15}")
for i in range(len(original_prices)):
    print(f"Item {i+1:<5} Rs. {original_prices[i]:>8,.2f}   Rs. {discounted_prices[i]:>10,.2f}")

print(f"\nOriginal total : Rs. {sum(original_prices):,.2f}")
print(f"Sale total     : Rs. {sum(discounted_prices):,.2f}")
print(f"You save       : Rs. {sum(original_prices) - sum(discounted_prices):,.2f}")
