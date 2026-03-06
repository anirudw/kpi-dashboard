from data.data_loader import load_data
from visualisation.month_over_month_vis import plot_mom_growth
from visualisation.churned_comp_vis import churn_num_plot
from visualisation.top_ten_vis import plot_top_ten

import streamlit as st

mom, tot_customers,tot_revenue, top_ten, profile, churn, churn_num, churn_rate = load_data()

mom_fig = plot_mom_growth(mom)
churn_num_fig = churn_num_plot(churn_num)
top_ten_fig = plot_top_ten(top_ten)

# ---------------------------------------------------------------------------------

st.set_page_config(
    page_title="Retail KPI Dashboard",
    layout="wide"
)
st.title("Retail KPI Dashboard")

col1, col2, col3= st.columns(3)
col1.metric("Total Customers: ", tot_customers)
col2.metric("Total Revenue: ", f"${tot_revenue:,.0f}")
col3.metric("Churn Rate: ", f"{churn_rate:.2f}%")

st.subheader("Month Over Month Growth")
st.pyplot(mom_fig)

st.subheader("Top Ten Customers")
st.pyplot(top_ten_fig)

st.subheader("Churn Rate")
st.pyplot(churn_num_fig)



st.markdown("---")
st.caption("Dataset: Online Retail II (2010–2011)")
st.caption("Built with Python, PostgreSQL, Streamlit")