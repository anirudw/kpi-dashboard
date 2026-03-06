import streamlit as st
from data.connection import get_connection
from data.querries import fetch_profile, fetch_churn, fetch_mom
from data.processing import process_customer_churn, process_customer_profile, process_mom_data

@st.cache_data
def load_data():
    connection = get_connection()
   
    mom, tot_revenue = process_mom_data(fetch_mom(connection))
    churn, churn_num,churn_rate,tot_customers = process_customer_churn(fetch_churn(connection))
    profile, top_ten = process_customer_profile(fetch_profile(connection))

    return (mom, tot_customers,tot_revenue, top_ten, profile, churn, churn_num, churn_rate)
    