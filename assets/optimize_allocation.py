"""Independently verify a long-only maximum-Sharpe fund allocation.

Usage: python scripts/optimize_allocation.py path/to/authorized_course_file.xlsx

Do not redistribute course materials unless permission allows doing so.
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar


def main(path):
    df = pd.read_excel(path, header=1)
    required = {'Date', 'VBTLX', 'VFIAX'}
    if not required.issubset(df.columns):
        raise ValueError(f'Expected columns: {required}. Available: {list(df.columns)}')
    dates = pd.to_datetime(df['Date'])
    selection = df.loc[(dates >= '2012-01-01') & (dates < '2016-01-01'), ['VBTLX', 'VFIAX']].dropna()
    if len(selection) != 48:
        raise ValueError(f'Expected 48 monthly observations from Jan 2012–Dec 2015, got {len(selection)}')
    returns = selection.to_numpy(dtype=float) / 100  # Excel displays 0.88 as 0.88%
    mu = returns.mean(axis=0)
    cov = np.cov(returns, rowvar=False, ddof=1)

    def negative_sharpe(vbtlx_weight):
        weights = np.array([vbtlx_weight, 1 - vbtlx_weight])
        avg = weights @ mu
        risk = np.sqrt(weights @ cov @ weights)
        return -avg/risk

    result = minimize_scalar(negative_sharpe, bounds=(0,1), method='bounded', options={'xatol': 1e-12})
    if not result.success:
        raise RuntimeError(result.message)
    print(f'Optimal long-only VBTLX weight: {result.x*100:.4f}%')
    print(f'Optimal long-only VFIAX weight: {(1-result.x)*100:.4f}%')
    print(f'Historical monthly Sharpe ratio (rf=0): {-result.fun:.4f}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python scripts/optimize_allocation.py path/to/course_returns.xlsx')
    main(Path(sys.argv[1]))
