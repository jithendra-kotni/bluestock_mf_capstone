# Data Dictionary
## Bluestock Fintech | Mutual Fund Analytics Capstone

---

## 1. fact_nav (source: 02_nav_history.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Unique fund identifier |
| nav_date | DATE | Date of NAV |
| nav | REAL | Net Asset Value |

---

## 2. dim_fund (source: 07_scheme_performance.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Primary key |
| scheme_name | TEXT | Full fund name |
| fund_house | TEXT | AMC name |
| category | TEXT | Equity/Debt etc |
| plan | TEXT | Direct/Regular |
| expense_ratio_pct | REAL | Annual expense % |
| risk_grade | TEXT | Low/Moderate/High |

---

## 3. fact_transactions (source: 08_investor_transactions.csv)
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | TEXT | Fund identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| kyc_status | TEXT | Verified/Pending |

---

## 4. fact_performance (source: 07_scheme_performance.csv)
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | TEXT | Fund identifier |
| return_1yr_pct | REAL | 1 year return % |
| return_3yr_pct | REAL | 3 year return % |
| return_5yr_pct | REAL | 5 year return % |
| sharpe_ratio | REAL | Risk-adjusted return |
| beta | REAL | Market sensitivity |
| alpha | REAL | Excess return |
| aum_crore | REAL | Assets under management |