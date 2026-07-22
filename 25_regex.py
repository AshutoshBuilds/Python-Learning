"""
Lesson 25: Regular Expressions (re module)
==========================================
Validate PAN, email, and invoice IDs using pattern matching.
Essential for data cleaning in accounting and compliance.

Run: python 25_regex.py
"""

import re

# =============================================================================
# CONCEPT
# =============================================================================
# Regular expressions describe text patterns.
#
#   re.match(pattern, text)   — match at start
#   re.search(pattern, text)  — match anywhere
#   re.findall(pattern, text) — all matches
#
# Common symbols:
#   ^ $     start / end of string
#   \d      digit
#   [A-Z]   uppercase letter
#   {5}     exactly 5 times
#   +       one or more
#
# Indian PAN format: ABCDE1234F (5 letters, 4 digits, 1 letter)

print("=" * 60)
print("LESSON 25: Regular Expressions")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

# PAN: 5 uppercase letters + 4 digits + 1 uppercase letter
PAN_PATTERN = re.compile(r"^[A-Z]{5}\d{4}[A-Z]$")

# Simple business email pattern
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Invoice ID: INV- followed by 4 digits
INVOICE_ID_PATTERN = re.compile(r"^INV-\d{4}$")

# GSTIN (bonus): 15-char alphanumeric — useful in commerce
GSTIN_PATTERN = re.compile(r"^\d{2}[A-Z]{5}\d{4}[A-Z][A-Z0-9]Z[A-Z0-9]$")


def validate_pan(pan):
    return bool(PAN_PATTERN.match(pan.strip().upper()))


def validate_email(email):
    return bool(EMAIL_PATTERN.match(email.strip()))


def validate_invoice_id(inv_id):
    return bool(INVOICE_ID_PATTERN.match(inv_id.strip().upper()))


def extract_invoice_ids_from_text(text):
    """Find all INV-#### patterns in a block of text."""
    return re.findall(r"INV-\d{4}", text.upper())


# --- Sample data to validate ---
pan_samples = [
    "ABCDE1234F",   # valid
    "abcde1234f",   # valid after upper()
    "ABCD1234F",    # invalid — only 4 letters
    "ABCDE12345",   # invalid — ends with digit
]

email_samples = [
    "accounts@sharmatraders.com",
    "invalid-email",
    "gst.help@mehta-bank.co.in",
    "@nodomain.com",
]

invoice_samples = [
    "INV-1001",
    "inv-1002",
    "INV-99",
    "BILL-1001",
]

print("\n--- PAN Validation ---")
for pan in pan_samples:
    status = "VALID" if validate_pan(pan) else "INVALID"
    print(f"  {pan:15} -> {status}")

print("\n--- Email Validation ---")
for email in email_samples:
    status = "VALID" if validate_email(email) else "INVALID"
    print(f"  {email:35} -> {status}")

print("\n--- Invoice ID Validation ---")
for inv in invoice_samples:
    status = "VALID" if validate_invoice_id(inv) else "INVALID"
    print(f"  {inv:12} -> {status}")

# --- Extract invoice IDs from messy text ---
print("\n--- Extract Invoice IDs from Text ---")
audit_log = """
Payment received against INV-1001 and INV-1003.
Credit note issued for inv-1005. Ref: INV-9999 is a typo.
"""
found = extract_invoice_ids_from_text(audit_log)
print(f"  Found: {found}")

# --- GSTIN bonus demo ---
print("\n--- GSTIN Validation (bonus) ---")
gstin_samples = ["27AABCS1234F1Z5", "27AABCS1234F1Z", "INVALID"]
for g in gstin_samples:
    ok = bool(GSTIN_PATTERN.match(g))
    print(f"  {g:20} -> {'VALID' if ok else 'INVALID'}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Validate PAN "AABCP1234K" — expect True.

# print(validate_pan("AABCP1234K"))

# Exercise 2: Write a pattern for amounts like "Rs 1,250.00" and test one match.
# Hint: Rs\s[\d,]+\.\d{2}

# amount_pattern = re.compile(r"Rs\s[\d,]+\.\d{2}")
# text = "Total payable: Rs 1,250.00 plus GST"
# m = amount_pattern.search(text)
# print(m.group() if m else "No match")

# Exercise 3: Extract all emails from a string using re.findall.

# blob = "Contact billing@acme.com or support@acme.org for help."
# emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", blob)
# print(emails)


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
Given a list of vendor records (PAN, email, invoice_id), validate each
and print a compliance report: PASS or FAIL per field.
""")

# --- Mini challenge reference solution ---
vendors = [
    {"name": "Sharma Traders", "pan": "ABCDE1234F", "email": "gst@sharma.com", "invoice": "INV-1001"},
    {"name": "Bad Data Co", "pan": "ABC12", "email": "not-an-email", "invoice": "INV-12"},
    {"name": "Mehta Supplies", "pan": "FGHIJ5678K", "email": "orders@mehta.co.in", "invoice": "INV-1011"},
]

print("\nChallenge result:")
for v in vendors:
    pan_ok = validate_pan(v["pan"])
    email_ok = validate_email(v["email"])
    inv_ok = validate_invoice_id(v["invoice"])
    overall = "PASS" if all([pan_ok, email_ok, inv_ok]) else "FAIL"
    print(f"  {v['name']:18} PAN:{pan_ok!s:5} Email:{email_ok!s:5} Inv:{inv_ok!s:5} -> {overall}")

print("\nLesson 25 complete.")
