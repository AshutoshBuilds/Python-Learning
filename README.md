# Python Course for Commerce Students

Teach Python from **basics to mastery** using real bank, tax, and business examples.

## How to use

1. Open files in number order: `01_...` → `38_...`
2. Run each file top-to-bottom (`python 01_introduction.py`)
3. Pause at **EXERCISES** — student tries first; solutions are in comments
4. Finish with the **MINI CHALLENGE**
5. Do capstone projects (35–37) only after lessons 01–34

## Setup

```bash
# From project root (optional venv)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Early lessons need no extra packages.
# For lessons 27–32 and projects:
pip install pandas openpyxl matplotlib requests
```

Sample data for later lessons lives in `data/`.

## Lesson map

| # | File | Focus |
|---|------|--------|
| 01–07 | Intro → conditionals | Foundations |
| 08–13 | Lists → loop control | Collections & loops |
| 14–20 | Functions → modules | Reusable code & files |
| 21–26 | OOP → datetime | Intermediate mastery |
| 27–34 | APIs, pandas, Excel, DB, testing, pip | Professional tools |
| 35–37 | Invoice / expense / sales projects | Capstones |
| 38 | Cheatsheet | Quick revision |

Every lesson uses practical scenarios: GST, invoices, interest, ledgers, P&L, banking ops.
