# Bluestock Fintech — Mutual Fund Analytics Capstone

## Project Overview
End-to-end mutual fund analytics platform analyzing 40 funds across 5 years (2022–2026).

## Setup Instructions
1. Clone the repo:
   git clone https://github.com/jithendra-kotni/bluestock_mf_capstone.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run ETL pipeline:
   python scripts/etl_pipeline.py

4. Open dashboard:
   Open dashboard/bluestock_mf_dashboard.pbix in Power BI Desktop

## File Descriptions
- scripts/etl_pipeline.py — Main ETL pipeline
- scripts/live_nav_fetch.py — Fetch live NAV from mfapi.in
- scripts/recommender.py — Fund recommendation engine
- notebooks/ — Analysis notebooks (Day 1-6)
- sql/schema.sql — SQLite database schema
- sql/queries.sql — 10 analytical SQL queries
- data/processed/ — Cleaned CSV files
- data/db/ — SQLite database
- dashboard/ — Power BI dashboard
- reports/ — Final report and charts

## How to Run
python scripts/etl_pipeline.py