# Methodology, Assumptions, and Limitations

## Problem and source material

The original submission is a **five-slide PowerPoint** prepared for the Business and Financial Modeling Capstone. Its focus is Step 5 of the course case: choosing an optimal risky allocation between two index funds and comparing it with a single equity holding.

- **Estimation window:** January 2012–December 2015 (48 monthly returns).
- **Fund inputs:** VBTLX (bonds) and VFIAX (equities), using a monthly returns dataset provided through the course.
- **Comparison window:** January–July 2016 (7 months).
- **Comparison security:** AAPL, using return figures in the submitted presentation.
- **Starting capital:** $5,000,000; hypothetical (no fees or taxes modeled).
- **Portfolio convention:** long-only, no leverage, allocation weights sum to 1, constant portfolio weights for the seven-month comparison.
- **Risk-free rate:** 0%, per the course instructions.

## Portfolio optimization

The objective maximizes historical Sharpe ratio:

```text
portfolio_return = w · mean(monthly_returns)
portfolio_risk   = sqrt(wᵀ · covariance(monthly_returns) · w)
Sharpe_ratio     = portfolio_return / portfolio_risk   # r_f = 0
constraints: w_VBTLX + w_VFIAX = 1; 0 <= weights <= 1
```

The allocation in the original slides is **VBTLX 67.8459%** and **VFIAX 32.1541%**. Independently optimizing the course-provided monthly fund returns for 2012–2015 yields approximately the same allocation, with small rounding differences.

## Performance measurement

The student-authored PowerPoint embeds a chart with the monthly returns published in `data/reported_monthly_returns_2016.csv`. Values in that CSV were extracted from the student's presentation, not copied from a current market feed.

Cumulative returns are calculated as `product(1 + r_t) − 1`. Monthly volatility uses the sample standard deviation (`ddof=1`) of the seven monthly percent return observations. Results:

| Measure | Mixed portfolio | AAPL |
|:--|--:|--:|
| Cumulative return | 6.7683% | 10.2061% |
| Monthly standard deviation | 1.1087% | 9.0370% |
| Worst month | −0.6211% | −13.9921% |
| Ending value | $5,338,415 | $5,510,306 |

All values are shown rounded in the original slide deck.

## Interpretation and caveats

- The results compare only **seven subsequent months**, and are not evidence of performance in later markets.
- Estimation-window results may be sensitive to period selection and short historical samples.
- Index funds and individual equities differ in diversification, economic exposure, and risk.
- Trading fees, slippage, taxes, and investment restrictions beyond long-only weights were not modeled in the student slides.
- This repository **does not claim possession of the original submitted Solver spreadsheet**. A modern verification script is provided separately for anyone with an authorized copy of the source dataset.
- Course-provided raw historical datasets have not been republished in the public repository package.

**Educational analysis only; not financial advice.**
