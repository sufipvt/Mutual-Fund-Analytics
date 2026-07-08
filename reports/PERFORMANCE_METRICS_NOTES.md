# Performance Metrics Notes

# 1. Sharpe Ratio

## What is Sharpe Ratio?

Sharpe Ratio measures the **risk-adjusted return** of an investment.

It tells us:

> How much extra return did the investor earn for every unit of total risk taken?

A higher Sharpe Ratio indicates better performance.

---

## Why do we use it?

Suppose two mutual funds both generated **15% annual return**.

| Fund | Return | Risk |
|------|--------|------|
| A | 15% | High |
| B | 15% | Low |

Fund B is better because it achieved the same return with lower risk.

Sharpe Ratio helps identify such funds.

---

## Formula

Sharpe Ratio = (Rp − Rf) / σ × √252

Where:

- Rp = Average daily return
- Rf = Daily risk-free rate
- σ = Standard deviation of daily returns (volatility)
- √252 = Annualization factor

---

## Steps

### 1. Calculate Daily Returns

```python
nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
    .pct_change()
)
```

---

### 2. Average Daily Return

```python
mean_return = (
    nav_df.groupby("amfi_code")["daily_return"]
    .mean()
)
```

---

### 3. Daily Volatility

```python
volatility = (
    nav_df.groupby("amfi_code")["daily_return"]
    .std()
)
```

---

### 4. Risk-Free Rate

```python
risk_free_daily = 0.065 / 252
```

---

### 5. Compute Sharpe Ratio

```python
sharpe_df = pd.DataFrame({
    "mean_return": mean_return,
    "volatility": volatility
})

sharpe_df["sharpe_ratio"] = (
    (sharpe_df["mean_return"] - risk_free_daily)
    / sharpe_df["volatility"]
) * (252 ** 0.5)
```

---

## Interpretation

| Sharpe Ratio | Meaning |
|--------------|---------|
| < 0 | Poor |
| 0 – 1 | Average |
| 1 – 2 | Good |
| > 2 | Excellent |

---

# 2. Sortino Ratio

## What is Sortino Ratio?

Sortino Ratio measures the return earned for each unit of **downside risk**.

Unlike Sharpe Ratio, it ignores positive volatility.

---

## Why do we use it?

Positive returns are beneficial.

Only negative returns are considered risky.

Sortino Ratio penalizes only downside volatility.

---

## Formula

Sortino Ratio = (Rp − Rf) / Downside Deviation × √252

Where:

- Rp = Average daily return
- Rf = Daily risk-free rate
- Downside Deviation = Standard deviation of negative returns only

---

## Steps

### 1. Create Downside Return

```python
nav_df["downside_return"] = nav_df["daily_return"].clip(upper=0)
```

---

### 2. Downside Deviation

```python
downside_std = (
    nav_df.groupby("amfi_code")["downside_return"]
    .std()
)
```

---

### 3. Mean Return

```python
mean_return = (
    nav_df.groupby("amfi_code")["daily_return"]
    .mean()
)
```

---

### 4. Compute Sortino Ratio

```python
sortino_df = pd.DataFrame({
    "mean_return": mean_return,
    "downside_std": downside_std
})

sortino_df["sortino_ratio"] = (
    (sortino_df["mean_return"] - risk_free_daily)
    / sortino_df["downside_std"]
) * (252 ** 0.5)
```

---

## Sharpe vs Sortino

| Sharpe Ratio | Sortino Ratio |
|--------------|---------------|
| Uses total volatility | Uses downside volatility only |
| Penalizes positive and negative movements | Penalizes only negative movements |
| General risk measure | Downside risk measure |

---

## Interpretation

Higher Sortino Ratio indicates better downside risk-adjusted performance.

---

# 3. Alpha & Beta

## What is Beta?

Beta measures how sensitive a mutual fund is to market movements.

It tells us:

> If the market changes by 1%, how much will the fund move?

---

## Beta Interpretation

| Beta | Meaning |
|------|---------|
| 1.0 | Moves with the market |
| > 1 | More volatile than the market |
| < 1 | Less volatile than the market |
| 0 | No relationship with market |

---

## Examples

Market increases by 10%

| Beta | Expected Fund Return |
|------|----------------------|
| 1.2 | 12% |
| 1.0 | 10% |
| 0.8 | 8% |

---

# What is Alpha?

Alpha measures the fund's performance **after removing the effect of market movement**.

It answers:

> Did the fund outperform or underperform what was expected based on its Beta?

---

## Alpha Interpretation

| Alpha | Meaning |
|--------|---------|
| Positive | Outperformed market expectation |
| Zero | Performed as expected |
| Negative | Underperformed |

---

## Regression Equation

Fund Return = α + β × Market Return

Where

- α = Alpha (intercept)
- β = Beta (slope)

---

## Formula Used

Using Ordinary Least Squares (OLS):

```python
from scipy.stats import linregress

result = linregress(
    market_return,
    fund_return
)

beta = result.slope
alpha = result.intercept * 252
```

The intercept is multiplied by **252** to annualize Alpha.

---

## Why use Regression?

Regression finds the best-fit line between:

- Benchmark daily returns
- Mutual fund daily returns

The slope of the line is Beta.

The intercept is Alpha.

---

## Interpretation

Example

Beta = 1.15

Meaning:

> When the market increases by 1%, the fund is expected to increase by approximately 1.15%.

Alpha = 2.4%

Meaning:

> The fund generated approximately 2.4% additional annual return beyond what its market exposure would predict.

---

# Summary

| Metric | Measures | Higher is Better? |
|----------|----------|-------------------|
| Sharpe Ratio | Return per unit of total risk | Yes |
| Sortino Ratio | Return per unit of downside risk | Yes |
| Beta | Market sensitivity | Depends on investor preference |
| Alpha | Excess return over market expectation | Yes |

---

# Interview One-Liners

### Sharpe Ratio

"Measures excess return earned for each unit of total volatility."

### Sortino Ratio

"Measures excess return earned for each unit of downside risk."

### Beta

"Measures how sensitive a mutual fund is to market movements."

### Alpha

"Measures how much a fund outperformed or underperformed after accounting for market risk."
