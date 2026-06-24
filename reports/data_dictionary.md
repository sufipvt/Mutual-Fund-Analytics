# Data Dictionary — Mutual Fund Analytics

## dim_fund
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique ID for each mutual fund scheme (primary key) |
| fund_house | TEXT | Name of the AMC managing the fund (e.g. SBI Mutual Fund) |
| scheme_name | TEXT | Full name of the fund |
| category | TEXT | Equity or Debt |
| sub_category | TEXT | e.g. Large Cap, Small Cap, Liquid |
| plan | TEXT | Direct or Regular |
| launch_date | TEXT | Date the fund was launched |
| benchmark | TEXT | The index this fund is compared against |
| expense_ratio_pct | REAL | Annual fee charged, as % of investment |
| exit_load_pct | REAL | Penalty % charged for early withdrawal |
| fund_manager | TEXT | Name of the fund's manager |
| risk_category | TEXT | SEBI risk grade (Low/Moderate/High/Very High) |
| sebi_category_code | TEXT | SEBI's internal scheme code |

## dim_date
| Column | Type | Description |
|---|---|---|
| date_id | TEXT | Calendar date (YYYY-MM-DD), primary key |
| year | INTEGER | Year extracted from date |
| month | INTEGER | Month number (1-12) |
| quarter | INTEGER | Quarter number (1-4) |
| is_weekday | INTEGER | 1 if Mon-Fri, 0 if Sat/Sun |

## fact_nav
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Foreign key to dim_fund |
| date_id | TEXT | Foreign key to dim_date |
| nav | REAL | Net Asset Value (price per unit) on that date |

## fact_transactions
| Column | Type | Description |
|---|---|---|
| tx_id | INTEGER | Unique transaction ID (primary key, auto-generated) |
| investor_id | TEXT | Unique ID for the investor |
| amfi_code | INTEGER | Foreign key to dim_fund |
| transaction_date | TEXT | Date of the transaction |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in Indian Rupees |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | T30 (top 30 cities) or B30 (beyond top 30) |
| age_group | TEXT | Investor's age bracket |
| gender | TEXT | Male or Female |
| payment_mode | TEXT | UPI, Net Banking, Mandate, or Cheque |
| kyc_status | TEXT | Verified or Pending |

## fact_performance
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Foreign key to dim_fund |
| return_1yr_pct | REAL | 1-year return, % |
| return_3yr_pct | REAL | 3-year annualised return, % |
| return_5yr_pct | REAL | 5-year annualised return, % |
| sharpe_ratio | REAL | Risk-adjusted return measure (higher = better) |
| sortino_ratio | REAL | Like Sharpe, but only penalises downside risk |
| max_drawdown_pct | REAL | Worst peak-to-trough decline, % |
| aum_crore | REAL | Assets under management, in ₹ crore |
| morningstar_rating | INTEGER | Star rating, 1-5 |

## fact_aum
| Column | Type | Description |
|---|---|---|
| fund_house | TEXT | Name of the AMC |
| date | TEXT | Quarter-end date |
| aum_crore | REAL | Total assets under management for that fund house, ₹ crore |
| num_schemes | INTEGER | Number of schemes the fund house runs |