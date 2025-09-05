import streamlit as st
import pandas as pd

st.set_page_config(page_title="OPX3 Governance Dashboard", layout="wide")

# Load Excel file
df = pd.read_excel("OPX3_Governance_Tracker_v2.xlsx", sheet_name="Master Tracker")

st.title("📊 OPX3 Governance Dashboard")
st.markdown("Governance tracking for CMMI audit readiness.")

# Filters
status_filter = st.multiselect("Filter by Status", options=df["Status"].dropna().unique(), default=df["Status"].dropna().unique())
filtered_df = df[df["Status"].isin(status_filter)]

# Display
st.dataframe(filtered_df, use_container_width=True)

# Metrics
st.metric("Total Items", len(df))
st.metric("Completed", len(df[df["Status"] == "Done"]))
