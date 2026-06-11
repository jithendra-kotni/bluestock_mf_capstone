"""
dashboard.py - Streamlit Dashboard
Bluestock Fintech | Mutual Fund Analytics Capstone
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROC_DIR = BASE_DIR / "data" / "processed"

st.set_page_config(page_title="Bluestock MF Analytics", layout="wide")

# Load data
@st.cache_data
def load_data():
    nav  = pd.read_csv(PROC_DIR / "clean_nav.csv", parse_dates=["date"])
    txn  = pd.read_csv(PROC_DIR / "clean_transactions.csv", parse_dates=["transaction_date"])
    perf = pd.read_csv(PROC_DIR / "clean_performance.csv")
    score = pd.read_csv(PROC_DIR / "fund_scorecard.csv")
    return nav, txn, perf, score

nav, txn, perf, score = load_data()

# ── Header ───────────────────────────────────────────────────────
st.title("📊 Bluestock Fintech — Mutual Fund Analytics")
st.markdown("---")

# ── KPI Cards ────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total AUM", f"₹{perf['aum_crore'].sum()/100000:.2f}L Cr")
col2.metric("Total SIP Inflows", f"₹{txn['amount_inr'].sum()/1e9:.1f}Bn")
col3.metric("Total Investors", f"{txn['investor_id'].nunique():,}")
col4.metric("Total Schemes", f"{perf['amfi_code'].nunique()}")

st.markdown("---")

# ── Tabs ─────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["NAV Trends", "Fund Performance", "Investor Analytics", "Recommender"])

with tab1:
    st.subheader("NAV Trend Analysis")
    funds = st.multiselect("Select Funds", nav['amfi_code'].unique(), default=nav['amfi_code'].unique()[:5])
    filtered = nav[nav['amfi_code'].isin(funds)]
    fig = px.line(filtered, x="date", y="nav", color="amfi_code", title="NAV Trends 2022-2026")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Fund Scorecard")
    st.dataframe(score[['amfi_code', 'score', 'cagr_3yr', 'sharpe_ratio']].sort_values('score', ascending=False))

    fig2 = px.scatter(perf, x="return_3yr_pct", y="sharpe_ratio",
                      size="aum_crore", color="fund_house",
                      title="Return vs Risk")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Investor Analytics")
    col1, col2 = st.columns(2)

    with col1:
        age_data = txn['age_group'].value_counts().reset_index()
        fig3 = px.pie(age_data, names='age_group', values='count', title="Age Group Distribution")
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        state_data = txn.groupby('state')['amount_inr'].sum().reset_index()
        fig4 = px.bar(state_data.sort_values('amount_inr', ascending=False).head(10),
                      x='state', y='amount_inr', title="Top 10 States by SIP Amount")
        st.plotly_chart(fig4, use_container_width=True)

with tab4:
    st.subheader("Fund Recommender")
    risk = st.selectbox("Select Risk Appetite", ["Low", "Moderate", "High"])
    filtered_perf = perf[perf['risk_grade'].str.lower() == risk.lower()]
    top3 = filtered_perf.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'fund_house', 'risk_grade', 'sharpe_ratio', 'return_3yr_pct']
    ]
    st.dataframe(top3)