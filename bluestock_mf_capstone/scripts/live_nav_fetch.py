"""
live_nav_fetch.py

Task 4:
Fetch HDFC Top 100 NAV

Task 5:
Fetch NAV for 5 schemes and save each as CSV.
"""
import logging
import pandas as pd
import requests
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log=logging.getLogger(__name__)

BASE_DIR=Path(__file__).resolve().parent.parent
RAW_DIR= BASE_DIR/ "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

schemes={"SBI Bluechip":119551,"ICICI Bluechip":120503,"Nippon Large Cap":118632,"Axis Bluechip":119092,
"Kotak Bluechip":120841}

for scheme_name,scheme_code in schemes.items():
    try:
        URL=f"https://api.mfapi.in/mf/{scheme_code}"
        log.info("Fecthing NAV from mfapi.in...")
        response=requests.get(URL,timeout=30)
        response.raise_for_status()

        data=response.json()

        log.info(f"Fund : {data['meta']['scheme_name']}")
        log.info(f"Category : {data['meta']['scheme_category']}")

        df = pd.DataFrame(data['data'])
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
        df['nav']  = pd.to_numeric(df['nav'], errors='coerce')
        df.sort_values('date', inplace=True)

        print(df.head())
        print(f"Shape: {df.shape}")
        
        file_name=scheme_name.lower().replace(" ","_")
        out_path = RAW_DIR / f"{file_name}_nav.csv"
        df.to_csv(out_path, index=False)
        log.info(f"Saved → {out_path} ")

    except requests.exceptions.ConnectionError:
        log.error("No internet connection.")
    except requests.exceptions.Timeout:
        log.error("Request timed out.")
    except Exception as e:
        log.error(f"Something went wrong: {e}")