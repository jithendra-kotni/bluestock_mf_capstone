from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PROC_DIR = BASE_DIR / "data" / "processed"

perf = pd.read_csv(PROC_DIR / "clean_performance.csv")

def recommend_funds(risk_appetite: str) -> pd.DataFrame:
    """
    Input: risk_appetite = 'Low', 'Moderate', 'High'
    Output: Top 3 funds by Sharpe ratio within matching risk_grade
    """
    filtered = perf[perf['risk_grade'].str.lower() == risk_appetite.lower()]
    
    if filtered.empty:
        print(f"No funds found for risk appetite: {risk_appetite}")
        return pd.DataFrame()
    
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'fund_house', 'risk_grade', 'sharpe_ratio', 'return_3yr_pct']
    ]
    return top3

if __name__ == "__main__":
    for risk in ['Low', 'Moderate', 'High']:
        print(f"\n{'='*50}")
        print(f"Top 3 funds for {risk} risk appetite:")
        print(recommend_funds(risk).to_string(index=False))