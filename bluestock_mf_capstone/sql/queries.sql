-- Bluestock Fintech | Mutual Fund Analytics Capstone

-- 1. Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
JOIN dim_fund USING (amfi_code)
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT amfi_code,
       strftime('%Y-%m', nav_date) AS month,
       ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- 3. SIP inflow YoY growth
SELECT strftime('%Y', transaction_date) AS year,
       ROUND(SUM(amount_inr), 2) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions,
       ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense_ratio < 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- 6. Best performing funds (1yr return)
SELECT scheme_name, return_1yr_pct
FROM fact_performance
JOIN dim_fund USING (amfi_code)
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 7. Funds with negative Sharpe ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
JOIN dim_fund USING (amfi_code)
WHERE sharpe_ratio < 0;

-- 8. Total AUM by fund house
SELECT fund_house, ROUND(SUM(aum_crore), 2) AS total_aum
FROM fact_performance
JOIN dim_fund USING (amfi_code)
GROUP BY fund_house
ORDER BY total_aum DESC;

-- 9. Top investors by transaction amount
SELECT investor_id, ROUND(SUM(amount_inr), 2) AS total_invested
FROM fact_transactions
WHERE transaction_type != 'Redemption'
GROUP BY investor_id
ORDER BY total_invested DESC
LIMIT 10;

-- 10. Average return by category
SELECT category,
       ROUND(AVG(return_1yr_pct), 2) AS avg_1yr,
       ROUND(AVG(return_3yr_pct), 2) AS avg_3yr,
       ROUND(AVG(return_5yr_pct), 2) AS avg_5yr
FROM fact_performance
JOIN dim_fund USING (amfi_code)
GROUP BY category;