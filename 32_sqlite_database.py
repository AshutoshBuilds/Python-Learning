"""
Lesson 32: SQLite Database for a Simple Ledger
==============================================
Commerce focus: Store accounts and transactions like a mini banking ledger.
"""

import sqlite3
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# SQLite is a file-based database — no separate server needed.
# Use context managers (with conn:) so connections close automatically.
# CREATE TABLE IF NOT EXISTS + DELETE keeps scripts idempotent (safe re-run).
# ---------------------------------------------------------------------------

DB_PATH = Path(__file__).parent / "data" / "ledger_demo.db"


def setup_database(db_path: Path) -> sqlite3.Connection:
    """Create tables and return an open connection."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    with conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS accounts (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                type TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS transactions (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER NOT NULL,
                amount     REAL NOT NULL,
                note       TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts(id)
            );
            DELETE FROM transactions;
            DELETE FROM accounts;
            """
        )
    return conn


def seed_sample_data(conn: sqlite3.Connection) -> None:
    """Insert demo accounts and transactions."""
    with conn:
        conn.executemany(
            "INSERT INTO accounts (name, type) VALUES (?, ?)",
            [
                ("Cash Counter", "asset"),
                ("HDFC Current", "asset"),
                ("Sales Income", "income"),
                ("Rent Expense", "expense"),
            ],
        )
        cursor = conn.execute("SELECT id, name FROM accounts")
        acct = {row["name"]: row["id"] for row in cursor.fetchall()}

        conn.executemany(
            "INSERT INTO transactions (account_id, amount, note) VALUES (?, ?, ?)",
            [
                (acct["Sales Income"], 50000, "January sales"),
                (acct["Cash Counter"], 50000, "Cash received"),
                (acct["Rent Expense"], -25000, "Shop rent"),
                (acct["HDFC Current"], -25000, "Rent NEFT"),
                (acct["Sales Income"], 62000, "February sales"),
                (acct["HDFC Current"], 62000, "February collection"),
            ],
        )


def query_balances(conn: sqlite3.Connection) -> list[dict]:
    """Return account name and net balance (sum of transactions)."""
    sql = """
        SELECT a.name, a.type, COALESCE(SUM(t.amount), 0) AS balance
        FROM accounts a
        LEFT JOIN transactions t ON t.account_id = a.id
        GROUP BY a.id
        ORDER BY a.name
    """
    cursor = conn.execute(sql)
    return [dict(row) for row in cursor.fetchall()]


def main() -> None:
    # Idempotent start: remove old DB so each run is fresh
    if DB_PATH.exists():
        DB_PATH.unlink()

    # LIVE DEMOS
    with setup_database(DB_PATH) as conn:
        seed_sample_data(conn)
        balances = query_balances(conn)

    print("LIVE DEMO — SQLite ledger")
    print(f"  Database: {DB_PATH}")
    print("  Account balances:")
    for row in balances:
        print(f"    {row['name']:20} ({row['type']:8}) Rs. {row['balance']:>10,.2f}")

    income = sum(r["balance"] for r in balances if r["type"] == "income")
    expenses = sum(r["balance"] for r in balances if r["type"] == "expense")
    print(f"\n  Total income recorded : Rs. {income:,.2f}")
    print(f"  Total expenses recorded: Rs. {expenses:,.2f}")

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Write a query that returns only accounts with balance > 0.
    # 2) Add a transaction: Marketing expense Rs. 2500 from HDFC Current.
    #
    # Solution 1:
    #   conn.execute(
    #       "SELECT name, SUM(amount) AS bal FROM ... HAVING bal > 0"
    #   )
    #
    # Solution 2:
    #   with conn:
    #       conn.execute(
    #           "INSERT INTO transactions (account_id, amount, note) "
    #           "VALUES (?, ?, ?)",
    #           (acct["HDFC Current"], -2500, "Flyers"),
    #       )
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Add a `date` column to transactions, insert 3 dated entries,
    # and query total debits for a given month.


if __name__ == "__main__":
    main()
