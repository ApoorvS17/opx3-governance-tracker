import streamlit as st
import pandas as pd

st.set_page_config(page_title="OPX3 Governance Dashboard", layout="wide")

# Load the Excel file
df = pd.read_excel("OPX3_Governance_Tracker_v2.xlsx", sheet_name="Master Tracker", engine="openpyxl")

# Fill missing values to group properly
df["Stage"] = df["Stage"].fillna(method="ffill")
df["Governance Pointer"] = df["Governance Pointer"].fillna(method="ffill")
df["Status"] = df["Status"].fillna("N/A")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
stage_options = df["Stage"].unique().tolist()
stage_filter = st.sidebar.multiselect("Filter by Stage", options=stage_options, default=stage_options)

pointer_options = df["Governance Pointer"].unique().tolist()
pointer_filter = st.sidebar.multiselect("Filter by Governance Pointer", options=pointer_options, default=pointer_options)

status_options = df["Status"].unique().tolist()
status_filter = st.sidebar.multiselect("Filter by Status", options=status_options, default=status_options)

# Apply filters
filtered_df = df[
    df["Stage"].isin(stage_filter) &
    df["Governance Pointer"].isin(pointer_filter) &
    df["Status"].isin(status_filter)
]

# Dashboard metrics
st.title("📊 OPX3 Governance Dashboard")
st.markdown("Governance tracking for CMMI audit readiness.")
st.metric("Total Items", len(df))
st.metric("Filtered Items", len(filtered_df))
st.metric("Completed", len(filtered_df[filtered_df["Status"] == "Done"]))

# Display grouped data
for stage in filtered_df["Stage"].unique():
    stage_df = filtered_df[filtered_df["Stage"] == stage]
    st.subheader(f"📁 Stage: {stage}")
    for pointer in stage_df["Governance Pointer"].unique():
        pointer_df = stage_df[stage_df["Governance Pointer"] == pointer]
        with st.expander(f"🔸 Governance Pointer: {pointer} ({len(pointer_df)} items)", expanded=False):
            st.dataframe(pointer_df.reset_index(drop=True), use_container_width=True)
