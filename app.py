import streamlit as st

st.title("Retail business dashboard")

st.header("Header")
st.write("Message")

st.number_input()

age = st.number_input("Enter monthly Sales Target (in USD):",
                      min_value=0
                      max_value+10000,
                      value=50000)
filtered_data['Expenses'].sum():,.0f}")
col3.metric("Profit", f"${(filtered_data['Sales'].sum() - filtered_data['Expenses'].sum()):,.0f}")
