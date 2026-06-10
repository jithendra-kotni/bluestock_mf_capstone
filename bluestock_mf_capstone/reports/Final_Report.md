# Bluestock Fintech — Mutual Fund Analytics Capstone
## Final Report

---

## 1. Executive Summary
This project delivers a comprehensive mutual fund analytics platform analyzing 40 funds across 5 years (2022–2026). Key deliverables include an ETL pipeline, SQLite database, EDA notebooks, performance metrics, Power BI dashboard, and advanced analytics.

---

## 2. Data Sources & ETL
- **Source:** mfapi.in REST API + 10 CSV datasets
- **Funds analyzed:** 40 schemes across 10 AMCs
- **NAV records:** 46,000+ cleaned records
- **Pipeline:** `scripts/etl_pipeline.py` runs end-to-end without manual steps

---

## 3. EDA Findings
- Total AUM: ₹81L Crore across all funds
- SIP inflows reached ₹31,002 Cr milestone in Dec 2025
- T30 cities dominate 65% of transactions
- 56+ age group leads SIP participation

---

## 4. Performance Analysis
- Best Sharpe ratio: ICICI Pru Liquid Fund (7.68)
- Highest 3yr CAGR: Small Cap funds averaging 22%
- Maximum drawdown worst period: 2024 corrections
- 1,332 SIP investors flagged as at-risk

---

## 5. Dashboard Screenshots
- Page 1: Industry Overview
- Page 2: Fund Performance
- Page 3: Investor Analytics
- Page 4: SIP & Market Trends

---

## 6. Recommendations
- Investors with Low risk → Liquid funds (Sharpe > 5)
- Investors with High risk → Mid/Small Cap (3yr return > 18%)
- Flag and re-engage 1,332 at-risk SIP investors

---

## 7. Limitations
- NAV data limited to mfapi.in coverage
- No real-time portfolio rebalancing
- Sector weights approximated via category