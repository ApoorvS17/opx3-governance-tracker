import streamlit as st
import pandas as pd

st.set_page_config(page_title="OPX3 Governance Dashboard", layout="wide")

# Load the Excel file
df = pd.read_excel("OPX3_Governance_Tracker_v2.xlsx", sheet_name="Master Tracker", engine="openpyxl")

# Fill missing 'Stage' values forward to group sections
df["Stage"] = df["Stage"].fillna(method="ffill")

# Clean up Status column
df["Status"] = df["Status"].fillna("N/A")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
status_options = df["Status"].unique().tolist()
status_filter = st.sidebar.multiselect("Filter by Status", options=status_options, default=status_options)

owner_options = df["Owner"].dropna().unique().tolist()
owner_filter = st.sidebar.multiselect("Filter by Owner", options=owner_options, default=owner_options)

# Apply filters
filtered_df = df[df["Status"].isin(status_filter)]
filtered_df = filtered_df[filtered_df["Owner"].fillna("").isin(owner_filter)]

# Display metrics
st.title("📊 OPX3 Governance Dashboard")
st.markdown("Governance tracking for CMMI audit readiness.")
st.metric("Total Items", len(df))
st.metric("Filtered Items", len(filtered_df))
st.metric("Completed", len(filtered_df[filtered_df["Status"] == "Done"]))

# Group by Stage and display in collapsible sections
for stage in filtered_df["Stage"].unique():
    stage_df = filtered_df[filtered_df["Stage"] == stage]
    with st.expander(f"📁 {stage} ({len(stage_df)} items)", expanded=False):
        st.dataframe(stage_df.reset_index(drop=True), use_container_width=True)
