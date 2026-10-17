# Reproduce / inspect the results

The project is an **Excel-based course capstone**, not originally a Python software project. Python verification utilities were added later to make the presented figures inspectable.

## Check performance metrics using repository data

```bash
python -m pip install -r requirements.txt
python scripts/recalculate_performance.py
```

The script uses `data/reported_monthly_returns_2016.csv` extracted from the user's slide chart. It recomputes cumulative returns, monthly sample volatility, worst months, and starting-capital end values.

## Recheck 2012–2015 fund allocation using authorized course data

Download the course-provided **VBTLX-and-VFIAX-Monthly-Returns.xlsx** privately through your Coursera account, then run:

```bash
python scripts/optimize_allocation.py '/path/to/VBTLX-and-VFIAX-Monthly-Returns.xlsx'
```

The workbook layout is expected to have `Date`, `VBTLX`, and `VFIAX` columns on the second row with percentage values (e.g. `0.88` for 0.88%). The script filters dates before January 2016 and solves for the long-only maximum-Sharpe portfolio at `r_f=0`.

**Rights note:** The course dataset is not included with this GitHub repository; only files authored by the project owner and the numeric outputs reported in the presentation are included.
