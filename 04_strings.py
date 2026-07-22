"""
Lesson 04: Strings
Learning goals: Indexing, slicing, common string methods, and f-strings for
                invoice text, PAN masking, and customer name formatting.
Why commerce cares: Invoices, emails, SMS payment reminders, and GST filings are all text.
                    Python strings let you format, clean, and mask sensitive data.
"""

# =============================================================================
# CONCEPT
# =============================================================================
# A string (str) is text in quotes: "Hello", 'INV-2024-001', """multi-line"""
#
# INDEXING (position starts at 0):
#   "GSTIN" → G=0, S=1, T=2, I=3, N=4
#   Negative index counts from end: N=-1, I=-2
#
# SLICING [start:end] — end is NOT included:
#   pan[0:5]   first 5 characters
#   name[1:]   from index 1 to end
#   id[-4:]    last 4 characters
#
# USEFUL METHODS:
#   .upper() / .lower()     — case conversion
#   .strip()                — remove leading/trailing spaces
#   .replace(old, new)      — substitute text
#   .split(sep)             — break into list (e.g. by comma)
#   .startswith() / .endswith()
#   len(s)                  — character count
#
# F-STRINGS: f"Total: Rs. {amount:,.2f}" — embed variables in text

# =============================================================================
# LIVE DEMOS (bank / tax / business)
# =============================================================================

print("=" * 50)
print("STRINGS — INVOICES, PAN, CUSTOMER NAMES")
print("=" * 50)

# --- Demo 1: Invoice header text ---
company = "NAVKAR ENTERPRISES PVT LTD"
address = "  12, MG Road, Ahmedabad - 380001  "
gstin = "24AAACN1234F1Z5"

print("\n--- Invoice Header ---")
print(company.upper())
print(address.strip())                    # remove accidental spaces
print(f"GSTIN: {gstin}")
print(f"Invoice No: INV-{2026}-0042")

# --- Demo 2: Indexing and slicing on GSTIN ---
# GSTIN format: 2-digit state + 10-char PAN + entity + Z + checksum
print("\n--- GSTIN Parsing ---")
print(f"Full GSTIN  : {gstin}")
print(f"State code  : {gstin[0:2]}")
print(f"PAN portion : {gstin[2:12]}")
print(f"Last char   : {gstin[-1]}")

# --- Demo 3: PAN masking for display (privacy on receipts) ---
pan = "ABCPK1234L"
masked_pan = pan[0:2] + "XXXXX" + pan[-2:]
print(f"\nPAN (full)    : {pan}")
print(f"PAN (masked)  : {masked_pan}")

# --- Demo 4: Customer name formatting ---
raw_name = "  priya  SHARMA  "
clean_name = raw_name.strip().title()   # "Priya Sharma"
first_name = clean_name.split()[0]
last_name = clean_name.split()[-1]

print("\n--- Customer Name Cleanup ---")
print(f"Raw input  : '{raw_name}'")
print(f"Formatted  : {clean_name}")
print(f"First name : {first_name}")
print(f"Last name  : {last_name}")

# --- Demo 5: Building invoice line with f-string ---
item = "Laser Printer"
hsn = "8443"
qty = 2
unit_price = 12500.00
line_total = qty * unit_price

invoice_line = (
    f"{item:<20} HSN:{hsn}  Qty:{qty:>3}  "
    f"@ Rs.{unit_price:>10,.2f}  = Rs.{line_total:>12,.2f}"
)
print("\n--- Invoice Line ---")
print(invoice_line)

# --- Demo 6: Payment reminder message ---
customer = "Vikram Traders"
amount_due = 45750.00
due_date = "15-Jul-2026"
reminder = (
    f"Dear {customer},\n"
    f"Payment of Rs. {amount_due:,.2f} is due by {due_date}. "
    f"Please ignore if already paid. - Navkar Enterprises"
)
print("\n--- Payment Reminder ---")
print(reminder)

# --- Demo 7: String checks for validation ---
ifsc = "HDFC0001234"
print(f"\nIFSC '{ifsc}' length OK? {len(ifsc) == 11}")
print(f"Starts with bank code HDFC? {ifsc.startswith('HDFC')}")

email = "accounts@client.co.in"
print(f"Email has @? {'@' in email}")
domain = email.split("@")[1]
print(f"Domain: {domain}")

# --- Demo 8: Multi-line terms on invoice ---
terms = """TERMS & CONDITIONS:
1. Goods once sold will not be taken back.
2. Subject to Ahmedabad jurisdiction.
3. E. & O.E."""
print("\n" + terms)

# =============================================================================
# EXERCISES
# =============================================================================
# Exercise 1: Store invoice_id = "INV-2026-100". Print first 3 and last 3 chars.
# Exercise 2: Clean "  RAJ  exports  " to title case. Print result.
# Exercise 3: Mask bank account "123456789012" — show only last 4 digits as ****89012

# --- Student code area ---
# inv = "INV-2026-100"
# print(inv[:3], inv[-3:])

# --- Solutions ---
# messy = "  RAJ  exports  "
# print(messy.strip().title())
# acct = "123456789012"
# print("X" * (len(acct)-4) + acct[-4:])

# =============================================================================
# MINI CHALLENGE
# =============================================================================
# Given customer record fields, build a one-line GST invoice summary string.
# Fields: buyer_name, gstin, taxable, cgst, sgst, total

print("\n--- MINI CHALLENGE: One-Line Summary ---")
buyer_name = "Sunrise Retail LLP"
buyer_gstin = "27AADFS1234G1Z8"
taxable = 85000.00
cgst = 7650.00
sgst = 7650.00
total = taxable + cgst + sgst

summary = (
    f"BILL TO: {buyer_name} | GSTIN: {buyer_gstin} | "
    f"Taxable: Rs.{taxable:,.2f} | CGST: Rs.{cgst:,.2f} | "
    f"SGST: Rs.{sgst:,.2f} | TOTAL: Rs.{total:,.2f}"
)
print(summary)

# Mask buyer GSTIN middle PAN portion for a customer-facing SMS
masked_gstin = buyer_gstin[:2] + buyer_gstin[2:4] + "XXXXX" + buyer_gstin[9:]
print(f"SMS-safe GSTIN: {masked_gstin}")
