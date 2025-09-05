import streamlit as st
import pandas as pd

st.set_page_config(page_title="OPX3 Governance Dashboard", layout="wide")

# Load Excel
df = pd.read_excel("OPX3_Governance_Tracker_v2.xlsx", sheet_name="Master Tracker")

st.title("📊 OPX3 Governance Dashboard")
st.markdown("Governance tracking for CMMI audit readiness.")

# Clean up Status column
df["Status"] = df["Status"].fillna("N/A")

# Filter by Status
status_options = df["Status"].unique().tolist()
status_filter = st.multiselect("Filter by Status", options=status_options, default=status_options)

filtered_df = df[df["Status"].isin(status_filter)]

# Show metrics
st.metric("Total Items", len(df))
st.metric("Completed", len(df[df["Status"] == "Done"]))

# Show filtered data or fallback message
if not filtered_df.empty:
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("No data matches the selected filters. Please adjust your selections.")

