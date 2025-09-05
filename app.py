# Display grouped data by Stage and Governance Pointer
for stage in filtered_df["Stage"].unique():
    stage_df = filtered_df[filtered_df["Stage"] == stage]
    st.subheader(f"📁 Stage: {stage}")
    for pointer in stage_df["Governance Pointer"].unique():
        pointer_df = stage_df[stage_df["Governance Pointer"] == pointer]
        with st.expander(f"Governance pointer: {pointer}", expanded=False):
            display_df = pointer_df[[
                "What to Do",
                "Evidence/Artifact",
                "Metric/Threshold",
                "Status",
                "Due Date",
                "Owner"
            ]].reset_index(drop=True)
            st.dataframe(display_df, use_container_width=True)
