"""
Lesson 27: JSON & API Basics
============================
Serialize invoice data to JSON files and optionally fetch live rates
from a public API. Gracefully handles missing network or requests package.

Run: python 27_json_apis_basics.py
"""

import json
from pathlib import Path

# =============================================================================
# CONCEPT
# =============================================================================
# JSON (JavaScript Object Notation) is the standard text format for APIs.
#
#   json.dumps(obj)  — Python dict -> JSON string
#   json.loads(str)  — JSON string -> Python dict
#   json.dump(obj, file)  — write to file
#   json.load(file)       — read from file
#
# APIs return JSON over HTTP. The `requests` library fetches URLs.
# Always use try/except for network code — it may fail offline.

print("=" * 60)
print("LESSON 27: JSON & API Basics")
print("=" * 60)


# =============================================================================
# LIVE DEMOS
# =============================================================================

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
INVOICE_JSON_PATH = DATA_DIR / "sample_invoice.json"


def build_sample_invoice():
    """Build a realistic GST invoice as a Python dict."""
    return {
        "invoice_id": "INV-1001",
        "date": "2026-01-05",
        "customer": {
            "name": "Sharma Traders",
            "gstin": "27AABCS1234F1Z5",
            "email": "accounts@sharmatraders.com",
        },
        "lines": [
            {"sku": "SKU-001", "description": "Ledger Book", "qty": 10, "unit_price": 120.0, "gst_rate": 0.12},
            {"sku": "SKU-002", "description": "Pen Box", "qty": 5, "unit_price": 80.0, "gst_rate": 0.12},
        ],
        "currency": "INR",
    }


def invoice_totals(invoice):
    """Compute subtotal, GST, and grand total from invoice dict."""
    subtotal = 0.0
    gst_total = 0.0
    for line in invoice["lines"]:
        line_sub = line["qty"] * line["unit_price"]
        line_gst = round(line_sub * line["gst_rate"], 2)
        subtotal += line_sub
        gst_total += line_gst
    return {
        "subtotal": round(subtotal, 2),
        "gst": round(gst_total, 2),
        "grand_total": round(subtotal + gst_total, 2),
    }


# --- Demo: Python dict to JSON string ---
print("\n--- JSON.dumps / loads ---")
invoice = build_sample_invoice()
json_text = json.dumps(invoice, indent=2)
print("JSON preview (first 300 chars):")
print(json_text[:300] + "...")

restored = json.loads(json_text)
print(f"\nRound-trip check: {restored['invoice_id']} for {restored['customer']['name']}")

# --- Demo: Write and read JSON file ---
print("\n--- JSON File Write / Read ---")
with open(INVOICE_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(invoice, f, indent=2)
print(f"Written: {INVOICE_JSON_PATH}")

with open(INVOICE_JSON_PATH, encoding="utf-8") as f:
    loaded_invoice = json.load(f)

totals = invoice_totals(loaded_invoice)
print(f"Invoice {loaded_invoice['invoice_id']} totals:")
print(f"  Subtotal:     Rs {totals['subtotal']:,.2f}")
print(f"  GST:          Rs {totals['gst']:,.2f}")
print(f"  Grand Total:  Rs {totals['grand_total']:,.2f}")

# --- Demo: Optional API fetch ---
print("\n--- Optional API Fetch (requests) ---")

try:
    import requests
except ImportError:
    print("  requests not installed — skipping live API demo.")
    print("  Install with: pip install requests")
    print("  Showing offline JSON rate snippet instead:")
    offline_rates = {"base": "INR", "date": "2026-01-01", "rates": {"USD": 0.012}}
    print(f"  {json.dumps(offline_rates, indent=2)}")
else:
    try:
        # Public API: exchange rates (no key required)
        url = "https://api.exchangerate-api.com/v4/latest/INR"
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        rates = response.json()

        print(f"Base currency: {rates.get('base', 'N/A')}")
        print(f"Date: {rates.get('date', 'N/A')}")
        usd_rate = rates.get("rates", {}).get("USD")
        if usd_rate:
            inr_amount = 100000
            usd_equiv = round(inr_amount * usd_rate, 2)
            print(f"Rs {inr_amount:,} approx = USD {usd_equiv:,.2f} (indicative)")
    except (requests.exceptions.RequestException, OSError) as err:
        print(f"  Network unavailable ({type(err).__name__}) — skipping live API.")
        print("  Offline JSON demo still works above.")

# --- Demo: List of invoices as JSON array ---
print("\n--- JSON Array of Invoices ---")
invoices_batch = [build_sample_invoice(), {**build_sample_invoice(), "invoice_id": "INV-1002"}]
batch_path = DATA_DIR / "invoices_batch.json"
with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(invoices_batch, f, indent=2)
print(f"Saved {len(invoices_batch)} invoices to {batch_path.name}")


# =============================================================================
# EXERCISES
# =============================================================================
print("\n" + "=" * 60)
print("EXERCISES (try yourself, then uncomment solutions)")
print("=" * 60)

# Exercise 1: Create a dict for a single expense {"vendor": "...", "amount": 500}.
# Print json.dumps result.

# expense = {"vendor": "Stationery Mart", "amount": 500}
# print(json.dumps(expense))

# Exercise 2: Read sample_invoice.json and print customer GSTIN.

# with open(INVOICE_JSON_PATH, encoding="utf-8") as f:
#     inv = json.load(f)
# print(inv["customer"]["gstin"])

# Exercise 3: Add a key "status": "PAID" to loaded invoice and re-save.

# with open(INVOICE_JSON_PATH, encoding="utf-8") as f:
#     inv = json.load(f)
# inv["status"] = "PAID"
# with open(INVOICE_JSON_PATH, "w", encoding="utf-8") as f:
#     json.dump(inv, f, indent=2)


# =============================================================================
# MINI CHALLENGE
# =============================================================================
print("\n" + "=" * 60)
print("MINI CHALLENGE")
print("=" * 60)
print("""
1. Build invoice dict for one line item (your choice).
2. Save to data/mini_invoice.json
3. Load it back, compute grand total with gst_rate 18%
4. Print a one-line summary string.
""")

# --- Mini challenge reference solution ---
mini = {
    "invoice_id": "INV-MINI",
    "customer": {"name": "Patel Retail"},
    "lines": [{"sku": "SKU-RICE", "description": "Rice 5kg", "qty": 4, "unit_price": 350.0, "gst_rate": 0.05}],
}
mini_path = DATA_DIR / "mini_invoice.json"
with open(mini_path, "w", encoding="utf-8") as f:
    json.dump(mini, f, indent=2)

with open(mini_path, encoding="utf-8") as f:
    loaded_mini = json.load(f)

mini_totals = invoice_totals(loaded_mini)
summary = (
    f"{loaded_mini['invoice_id']} | {loaded_mini['customer']['name']} | "
    f"Total Rs {mini_totals['grand_total']:,.2f}"
)
print(f"\nChallenge result: {summary}")

print("\nLesson 27 complete.")
