import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format="%(levelname)s | %(message)s")
log=logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

csv_files=sorted(RAW_DIR.glob("*.csv"))

if not csv_files:
    log.error(f"No CSV files found in {RAW_DIR}")

else:
    log.info(f" Found {len(csv_files)} CSV files")
    
    for file in csv_files:
        try:
            df=pd.read_csv(file)
            print(f"\n{'='*50}")
            print(f"Filename: {file.name}")
            print(f"Shape: {df.shape}")

            print("\nDtype")
            print(f"DType: {df.dtypes}")

            print("\nHead")
            print(f"Head : {df.head()}")
        except Exception as e:
            log.error(f"Failed to load{file.name} | {e}")