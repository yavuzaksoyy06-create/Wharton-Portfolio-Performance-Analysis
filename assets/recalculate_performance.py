"""Recalculate performance metrics from the author's reported chart observations.

This validation helper was created for the GitHub portfolio; the original
Wharton course project was completed in Excel and presented with PowerPoint.
"""
from pathlib import Path
import pandas as pd
import numpy as np

DATA = Path(__file__).resolve().parents[1] / 'data' / 'reported_monthly_returns_2016.csv'
STARTING_CAPITAL = 5_000_000

def metrics(observations_pct):
    r = np.asarray(observations_pct, dtype=float) / 100
    return {
        'cumulative_return_pct': 100 * (np.prod(1 + r) - 1),
        'monthly_volatility_pct': 100 * np.std(r, ddof=1),
        'worst_month_pct': 100 * np.min(r),
        'ending_value_usd': STARTING_CAPITAL * np.prod(1 + r),
    }

def main():
    df = pd.read_csv(DATA)
    assert len(df) == 7, 'Expected January–July 2016 observations'
    for col in ['diversified_portfolio_pct', 'aapl_pct']:
        print(col)
        for k, v in metrics(df[col]).items():
            print(f'  {k}: {v:,.4f}')

if __name__ == '__main__':
    main()
