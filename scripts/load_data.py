import sqlite3
import pandas as pd

connection = sqlite3.connect("data/db/mutual_fund.db")

# load dim fund

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

fund_master_for_db = fund_master[[
    "amfi_code", "fund_house", "scheme_name", "category", "sub_category",
    "plan", "launch_date", "benchmark", "expense_ratio_pct", "exit_load_pct",
    "fund_manager", "risk_category", "sebi_category_code"
]]

fund_master_for_db.to_sql('dim_fund', connection, if_exists="replace", index = False)
print("Loaded dim_fund:", len(fund_master_for_db), "rows")


# ---- Load dim_date ----
# We generate this ourselves: one row for every day from Jan 2022 to today's data range
all_dates = pd.date_range(start="2022-01-01", end="2026-05-31", freq="D")

dim_date = pd.DataFrame({
    "date_id": all_dates.strftime("%Y-%m-%d"),
    "year": all_dates.year,
    "month": all_dates.month,
    "quarter": all_dates.quarter,
    "is_weekday": all_dates.dayofweek < 5  # Mon-Fri = True, Sat/Sun = False
})

dim_date.to_sql("dim_date", connection, if_exists="replace", index=False)
print("Loaded dim_date:", len(dim_date), "rows")


# ---- Load fact_nav ----
nav_history = pd.read_csv("data/processed/02_nav_history_clean.csv")

fact_nav = nav_history[["amfi_code", "date", "nav"]].copy()
fact_nav = fact_nav.rename(columns={"date": "date_id"})

fact_nav.to_sql("fact_nav", connection, if_exists="replace", index=False)
print("Loaded fact_nav:", len(fact_nav), "rows")


# ---- Load fact_transactions ----
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

fact_transactions = transactions[[
    "investor_id", "amfi_code", "transaction_date", "transaction_type",
    "amount_inr", "state", "city", "city_tier", "age_group", "gender",
    "payment_mode", "kyc_status"
]]

fact_transactions.to_sql("fact_transactions", connection, if_exists="replace", index=False)
print("Loaded fact_transactions:", len(fact_transactions), "rows")


# ---- Load fact_performance ----
performance = pd.read_csv("data/processed/07_schema_performance_clean.csv")

fact_performance = performance[[
    "amfi_code", "return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
    "sharpe_ratio", "sortino_ratio", "max_drawdown_pct", "aum_crore",
    "morningstar_rating"
]]

fact_performance.to_sql("fact_performance", connection, if_exists="replace", index=False)
print("Loaded fact_performance:", len(fact_performance), "rows")


# ---- Verify everything loaded correctly ----
print()
print("===== VERIFICATION =====")
cursor = connection.cursor()
for table in ["dim_fund", "dim_date", "fact_nav", "fact_transactions", "fact_performance"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows in database")

connection.commit()
connection.close()
print("\nDone. Database saved to data/db/bluestock_mf.db")