# Cash Flow Register

*A lightweight cash-flow forecasting application for households.*

**A modern check register that looks forward instead of backward.**

---

🎯 **Not a full budgeting app.**  
*Cash Flow Register exists to solve a specific problem: manual cash-flow forecasts gradually become inaccurate as expected transactions drift from what actually happens.*

‣ Instead of replacing your entire financial workflow, this tool focuses on one job: *showing where your checking balance is likely headed*. 

‣ Uses expected paychecks and expenses that can be adjusted as reality unfolds.

‣ Think of it as a traditional check register- *but one that projects where your balance is going instead of simply recording where it's been*.

‣ It helps answer the question:

> **"Will we have enough money over the next few weeks?"**

🚀 It's essentially **a check register on steroids**—keeping a running projection of your balance while making it easy to reconcile your original plan with what actually happened.

## Why this exists

Many budgeting tools are broad and feature-heavy.  
This project is intentionally narrow:

- We needed better near-term cash predictions
- We needed to compare plan vs reality quickly
- We needed early warning when projected spendable cash was overstated

## What it does

- Enter expected paychecks and planned expenses
- Build a projected cash-flow timeline
- Import actual bank transactions from CSV
- Adjust expected dates and amounts inline as real transactions occur
- Preserve the original plan while reflecting actual cash movement
- View projected balances over time
- Flag potential shortfalls before they happen

## What it is **not**

- Not a full budgeting suite
- Not focused on long-term net worth tracking
- Not a substitute for full accounting software
- Not trying to model every personal finance category or strategy

## Tech stack

- **Django** for backend and server-side rendering
- **HTMX** for responsive interactions without heavy frontend complexity
- **SQLite** for simple local data storage

## Typical workflow

1. Enter expected income and upcoming expenses.
2. Review the projected running balance.
3. Import recent bank transactions from CSV.
4. Adjust dates or amounts inline to match reality.
5. Instantly recalculate the remaining forecast.

## Getting started

```bash
git clone https://github.com/CJLA/cash-flow-register.git
cd cash-flow-register

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## CSV import

- Export transactions from your bank as CSV
- Include core fields (date, description, amount)
- Import and review to keep forecasts grounded in actual activity

## Project direction

Potential future improvements include:

- Smarter reconciliation between expected and imported transactions
- Google Calendar integration for recurring payments
- Multiple checking and savings account support
- Progressive Web App (PWA)
- Mobile application
- Scenario planning for major upcoming expenses

## Contributing

Feedback and pull requests are welcome—especially improvements that make forecasts more accurate, easier to trust, and simpler to use.
