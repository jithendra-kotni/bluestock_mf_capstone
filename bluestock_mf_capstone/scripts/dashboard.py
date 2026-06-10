import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parent.parent
raw = base / "data" / "processed"

for f in ['clean_nav','clean_performance','clean_transactions','fund_scorecard','returns_computed']:
    df=pd.read_csv(raw/f'{f}.csv')
    print(f"\n{f}")
    print(df.columns.tolist())
    print(df.shape)
    print(df.head(2))