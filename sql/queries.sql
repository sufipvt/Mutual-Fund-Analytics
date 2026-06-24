-- top 5 funds by AUM
SELECT f.scheme_name, f.fund_house, p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

-- Funds with expense ratio under 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER by expense_ratio_pct asc;

-- Total transaction amount by transaction type
SELECT transaction_type, sum(amount_inr) as total_amount
FROM fact_transactions
GROUP by transaction_type
ORDER by total_amount DESC

-- Total transaction amount by state
SELECT state, sum(amount_inr) as total_amount
FROM fact_transactions
GROUP by state
ORDER by total_amount

--  Average transaction amount by age group
SELECT age_group, AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_amount DESC;

-- Count of transactions by KYC status
SELECT kyc_status, count(*) as num_transaction
FROM fact_transactions
GROUP by kyc_status;

-- Monthly transaction volume
SELECT strftime('%Y-%m', transaction_date) as month, count(*) as num_transaction
FROM fact_transaction
GROUP by month
ORDER by month;

