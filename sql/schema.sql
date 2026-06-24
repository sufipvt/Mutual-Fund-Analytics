-- dim_fund: one row per mutual fund scheme (from 01_fund_master.csv)
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

-- dim_date: one row per calendar date (we generate this ourselves, no source file)
CREATE TABLE dim_date (
    date_id TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    is_weekday INTEGER
);

-- fact_nav: daily price per fund (from 02_nav_history_clean.csv)
CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date_id TEXT,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- fact_transactions: every investor transaction (from 08_investor_transactions.csv)
CREATE TABLE fact_transactions (
    tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- fact_performance: performance metrics per fund (from 07_scheme_performance.csv)
CREATE TABLE fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    morningstar_rating INTEGER,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);