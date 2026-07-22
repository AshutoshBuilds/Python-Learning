"""
Lesson 35: Capstone — Invoice System
====================================
Commerce focus: Build GST invoices with CGST/SGST split for intra-state sales.
"""

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# An invoice lists line items, subtotal, GST, and grand total.
# Intra-state GST splits equally into CGST and SGST (each = GST rate / 2).
# Use functions for calculations and a class to hold invoice data.
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"


@dataclass
class LineItem:
    description: str
    qty: int
    unit_price: float
    gst_rate: float = 0.18

    @property
    def taxable_value(self) -> float:
        return round(self.qty * self.unit_price, 2)

    @property
    def gst_amount(self) -> float:
        return round(self.taxable_value * self.gst_rate, 2)

    @property
    def line_total(self) -> float:
        return round(self.taxable_value + self.gst_amount, 2)


@dataclass
class Invoice:
    invoice_no: str
    customer_name: str
    customer_gstin: str
    invoice_date: date
    items: list[LineItem] = field(default_factory=list)
    place_of_supply: str = "Maharashtra"

    def subtotal(self) -> float:
        return round(sum(i.taxable_value for i in self.items), 2)

    def total_gst(self) -> float:
        return round(sum(i.gst_amount for i in self.items), 2)

    def grand_total(self) -> float:
        return round(self.subtotal() + self.total_gst(), 2)

    def cgst_sgst_split(self) -> tuple[float, float]:
        """Intra-state: CGST and SGST each get half of total GST."""
        half = round(self.total_gst() / 2, 2)
        return half, half

    def formatted_text(self) -> str:
        lines = [
            "=" * 60,
            "TAX INVOICE",
            "=" * 60,
            f"Invoice No : {self.invoice_no}",
            f"Date       : {self.invoice_date.isoformat()}",
            f"Customer   : {self.customer_name}",
            f"GSTIN      : {self.customer_gstin}",
            f"Place      : {self.place_of_supply}",
            "-" * 60,
            f"{'Item':<28} {'Qty':>4} {'Rate':>8} {'GST%':>6} {'Amount':>10}",
            "-" * 60,
        ]
        for item in self.items:
            lines.append(
                f"{item.description:<28} {item.qty:>4} "
                f"{item.unit_price:>8,.2f} {item.gst_rate*100:>5.0f}% "
                f"{item.line_total:>10,.2f}"
            )
        cgst, sgst = self.cgst_sgst_split()
        lines.extend(
            [
                "-" * 60,
                f"{'Taxable Value':>50} {self.subtotal():>10,.2f}",
                f"{'CGST':>50} {cgst:>10,.2f}",
                f"{'SGST':>50} {sgst:>10,.2f}",
                f"{'Grand Total':>50} {self.grand_total():>10,.2f}",
                "=" * 60,
            ]
        )
        return "\n".join(lines)


def build_sample_invoice() -> Invoice:
    return Invoice(
        invoice_no="INV-2026-0042",
        customer_name="Sharma Traders",
        customer_gstin="27AABCS1234A1Z5",
        invoice_date=date(2026, 2, 15),
        items=[
            LineItem("Ledger Book A4", qty=10, unit_price=120, gst_rate=0.12),
            LineItem("Pen Box (12 pcs)", qty=5, unit_price=80, gst_rate=0.12),
            LineItem("USB Drive 32GB", qty=3, unit_price=450, gst_rate=0.18),
        ],
    )


def save_invoice_text(invoice: Invoice, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(invoice.formatted_text(), encoding="utf-8")


def main() -> None:
    # LIVE DEMOS
    invoice = build_sample_invoice()
    text = invoice.formatted_text()
    print("LIVE DEMO — Formatted invoice")
    print(text)

    out_path = DATA_DIR / "invoice_demo.txt"
    save_invoice_text(invoice, out_path)
    print(f"\nInvoice saved to: {out_path}")

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Add a LineItem for "GST Filing Service" qty=1, price=2500, rate 18%.
    # 2) Write a function discount_subtotal(invoice, percent) that reduces
    #    taxable value before GST.
    #
    # Solution 1:
    #   invoice.items.append(LineItem("GST Filing Service", 1, 2500, 0.18))
    #
    # Solution 2:
    #   def discount_subtotal(inv, pct):
    #       factor = 1 - pct / 100
    #       return round(inv.subtotal() * factor, 2)
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Support inter-state IGST (no CGST/SGST split) when place_of_supply
    # differs from seller state; print IGST line instead.


if __name__ == "__main__":
    main()
