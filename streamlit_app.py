
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# Sample Data Definition
# -----------------------
kpi_data = {
    "Total Time Saved via AI": "1,240 Hours",
    "Average Time Saved per Quote": "4.1 Hours",
    "AI Adoption Rate": "82%",
    "Avg Quote Turnaround Time (AI)": "8.5 Hours",
    "Avg Quote Turnaround Time (Manual)": "22.1 Hours"
}

property_time_saved = {
    "Property Type": ["Warehouse", "Office Building", "Multi-Family Apt", "Single-Family Home", "Retail Space"],
    "Avg Time Saved (h)": [7.8, 6.9, 5.1, 2.9, 2.1]
}

region_adoption = {
    "Region": ["West", "East", "Central", "North", "South"],
    "Adoption Rate (%)": [95, 91, 88, 81, 64]
}

quote_activity = pd.DataFrame([
    ["HUS-83491", "West", "Office Building", "2023-10-26", "Yes", 7.2, "Quote Sent"],
    ["HUS-83490", "South", "Single-Family Home", "2023-10-26", "No", 25.8, "Delayed"],
    ["HUS-83488", "Central", "Warehouse", "2023-10-25", "Yes", 9.1, "Quote Sent"],
    ["HUS-83487", "East", "Multi-Family Apt", "2023-10-25", "Yes", 8.5, "Quote Sent"],
    ["HUS-83485", "South", "Office Building", "2023-10-24", "No", 21.4, "Delayed"],
    ["HUS-83482", "North", "Retail Space", "2023-10-24", "Yes", 6.9, "Quote Sent"]
], columns=["Inspection ID", "Region", "Property Type", "Inspection Date", "AI Used?", "Turnaround Time", "Status"])

# -----------------------
# Streamlit App
# -----------------------
st.set_page_config(page_title="Hustad - Inspection-to-Quote Dashboard", layout="wide")
st.title("Hustad - Inspection-to-Quote Workflow Performance")

# Filters (static for now)
st.markdown("### Filters")
st.selectbox("Date Range", ["Last 30 Days", "Last 7 Days", "This Quarter"])
st.multiselect("Region", ["All", "West", "East", "Central", "North", "South"], default=["All"])
st.multiselect("Property Type", ["All", "Warehouse", "Office Building", "Multi-Family Apt", "Single-Family Home", "Retail Space"], default=["All"])

# KPIs
st.markdown("---")
st.markdown("### Overall Performance KPIs")
kpi_cols = st.columns(3)
kpi_cols[0].metric("Total Time Saved via AI", kpi_data["Total Time Saved via AI"], "+15% vs. prev 30d")
kpi_cols[1].metric("Average Time Saved per Quote", kpi_data["Average Time Saved per Quote"], "+0.2h vs. prev 30d")
kpi_cols[2].metric("AI Adoption Rate", kpi_data["AI Adoption Rate"], "-5% vs. prev 30d")

kpi_cols2 = st.columns(2)
kpi_cols2[0].metric("Avg Quote Turnaround Time (AI)", kpi_data["Avg Quote Turnaround Time (AI)"], "Goal: <10h")
kpi_cols2[1].metric("Avg Quote Turnaround Time (Manual)", kpi_data["Avg Quote Turnaround Time (Manual)"], "+13.6h delay")

# Charts
st.markdown("---")
st.markdown("### Delay Analysis: AI vs Manual Turnaround Time")
st.bar_chart(pd.DataFrame({"Turnaround Time (h)": [8.5, 22.1]}, index=["AI-Assisted", "Manual"]))

st.markdown("### Performance by Property Type (Avg Time Saved)")
st.plotly_chart(px.bar(pd.DataFrame(property_time_saved), x="Property Type", y="Avg Time Saved (h)", title="Time Saved by Property Type"))

st.markdown("### AI Adoption Rate by Region")
st.plotly_chart(px.bar(pd.DataFrame(region_adoption), x="Region", y="Adoption Rate (%)", color="Adoption Rate (%)", title="AI Adoption Rate by Region", range_y=[0,100]))

# Table
st.markdown("### Recent Quote Activity")
st.dataframe(quote_activity, use_container_width=True)

# Notes
st.markdown("---")
st.markdown("**How to Use This Dashboard:**")
st.markdown("- **Executives**: Focus on the top KPIs to measure AI ROI and business impact.")
st.markdown("- **Regional Managers**: Filter by region to check AI adoption and delays.")
st.markdown("- **Operations Staff**: Use the quote table for daily monitoring and investigations.")
