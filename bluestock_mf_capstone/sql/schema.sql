-- Bluestock Fintech | Mutual Fund Analytics Capstone

-- Dimension table: Fund details
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code         TEXT PRIMARY KEY,
    scheme_name       TEXT,
    fund_house        TEXT,
    category          TEXT,
    sub_category      TEXT,
    plan              TEXT,
    expense_ratio_pct REAL,
    risk_grade        TEXT
);

-- Fact table: NAV history
CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code    TEXT,
    nav_date     DATE,
    nav          REAL,
    daily_return REAL,
    PRIMARY KEY (amfi_code, nav_date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Fact table: Investor transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    investor_id      TEXT,
    transaction_date DATE,
    amfi_code        TEXT,
    transaction_type TEXT,
    amount_inr       REAL,
    kyc_status       TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Fact table: Scheme performance
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code          TEXT PRIMARY KEY,
    return_1yr_pct     REAL,
    return_3yr_pct     REAL,
    return_5yr_pct     REAL,
    sharpe_ratio       REAL,
    beta               REAL,
    alpha              REAL,
    aum_crore          REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);