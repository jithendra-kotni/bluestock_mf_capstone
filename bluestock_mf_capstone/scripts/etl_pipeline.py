"""
data_cleaning.py - Day 2: Data Cleaning
Bluestock Fintech | Mutual Fund Analytics Capstone
"""

from pathlib import Path
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

BASE_DIR  = Path(__file__).resolve().parent.parent
RAW_DIR   = BASE_DIR / "data" / "raw"
PROC_DIR  = BASE_DIR / "data" / "processed"
PROC_DIR.mkdir(parents=True, exist_ok=True)


# ── Task 1: Clean nav_history ────────────────────────────────────
def clean_nav_history():
    df = pd.read_csv(RAW_DIR / "02_nav_history.csv")
    log.info(f"NAV raw shape: {df.shape}")

    # Parse dates
    df['date'] = pd.to_datetime(df['date'])

    # Sort by amfi_code + date
    df.sort_values(['amfi_code', 'date'], inplace=True)

    # Forward-fill missing NAV (holidays/weekends)
    df = df.set_index('date').groupby('amfi_code')['nav'] \
           .apply(lambda x: x.reindex(
               pd.date_range(x.index.min(), x.index.max(), freq='D')
           ).ffill()).reset_index()
    df.columns = ['amfi_code', 'date', 'nav']

    # Remove duplicates
    df.drop_duplicates(subset=['amfi_code', 'date'], inplace=True)

    # Validate NAV > 0
    invalid = df[df['nav'] <= 0]
    if not invalid.empty:
        log.warning(f"Found {len(invalid)} rows with NAV <= 0, dropping them")
        df = df[df['nav'] > 0]

    log.info(f"NAV cleaned shape: {df.shape}")
    out = PROC_DIR / "clean_nav.csv"
    df.to_csv(out, index=False)
    log.info(f"Saved → {out} ✅")


# ── Task 2: Clean investor_transactions ─────────────────────────
def clean_transactions():
    df = pd.read_csv(RAW_DIR / "08_investor_transactions.csv")
    log.info(f"Transactions raw shape: {df.shape}")

    # Standardise transaction_type
    valid_types = ['SIP', 'Lumpsum', 'Redemption']
    df['transaction_type'] = df['transaction_type'].str.strip().str.title()
    invalid_types = df[~df['transaction_type'].isin(valid_types)]
    if not invalid_types.empty:
        log.warning(f"Dropping {len(invalid_types)} rows with invalid transaction_type")
        df = df[df['transaction_type'].isin(valid_types)]

    # Validate amount > 0
    df = df[df['amount_inr'] > 0]

    # Check KYC status values
    log.info(f"KYC status values: {df['kyc_status'].unique()}")

    # Fix date format
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    log.info(f"Transactions cleaned shape: {df.shape}")
    out = PROC_DIR / "clean_transactions.csv"
    df.to_csv(out, index=False)
    log.info(f"Saved → {out} ✅")


# ── Task 3: Clean scheme_performance ────────────────────────────
def clean_performance():
    df = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")
    log.info(f"Performance raw shape: {df.shape}")

    # Validate return values are numeric
    return_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct']
    for col in return_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Flag negative Sharpe ratios
    negative_sharpe = df[df['sharpe_ratio'] < 0]
    if not negative_sharpe.empty:
        log.warning(f"{len(negative_sharpe)} funds have negative Sharpe ratio")

    # Check expense_ratio range (0.1% - 2.5%)
    out_of_range = df[~df['expense_ratio_pct'].between(0.1, 2.5)]
    if not out_of_range.empty:
        log.warning(f"{len(out_of_range)} funds have expense_ratio out of range")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    log.info(f"Performance cleaned shape: {df.shape}")
    out = PROC_DIR / "clean_performance.csv"
    df.to_csv(out, index=False)
    log.info(f"Saved → {out} ✅")


# ── Main ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    log.info("="*50)
    log.info("Starting Day 2 - Data Cleaning Pipeline")
    log.info("="*50)
    clean_nav_history()
    clean_transactions()
    clean_performance()
    log.info("\nAll cleaning done")