import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="OQVANTA",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style
.main {
    background-color: #f7f9fc;
}
.block-container {
    padding-top: 2rem;
}
.hero {
    background-color: #172033;
    padding: 25px;
    border-radius: 14px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    font-size: 38px;
    margin-bottom: 5px;
}

hero p {
    color: #cbd5e1;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>💳 OQVANTA</h1>
    <p>Failed Payment Recovery</p>
    <p>Track failed transactions and identify possible recovery opportunities.</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("OQVANTA/data/Transactions.csv")
successful_transactions = df[df["status"] == "success"]
failed_transactions = df[df["status"] == "failed"]
total_transactions = len(df)
successful_count = len(successful_transactions)/total_transactions if total_transactions > 0 else 0
failed_count = len(failed_transactions)/total_transactions if total_transactions > 0 else 0
revenue_lost = failed_transactions["amount"].sum()
highest_failed_value = failed_transactions["amount"].max()
st.subheader("Transaction Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Transactions", total_transactions)
with col2:
    st.metric("Successful", successful_count)
with col3:
    st.metric("Failed", failed_count)
with col4:
    st.metric("REVENUE IS AT RISK", f"₹{revenue_lost:,.0f}")

st.subheader("Failed Payment Methods")
failed_payment_methods = failed_transactions["payment"].value_counts()
st.bar_chart(failed_payment_methods)
st.subheader("Failed Transactions")
st.table(failed_transactions)
st.subheader("Recovery Opportunities")
col1, col2 = st.columns(2)
with col1:
    st.metric("Highest Failed Payment",f"₹{highest_failed_value:,.0f}")
with col2:
   high_priority = failed_transactions[ failed_transactions["amount"] > 800]
high_priority_amount = high_priority["amount"].sum()
st.metric( "High-Value Failed Payments",f"₹{high_priority_amount:,.0f}" )
if len(high_priority) > 0:

    st.write("Payments with higher priority to recover:")
    st.dataframe( high_priority, use_container_width=True )

st.subheader("RECOVERY ACTION PLAN")
if len(failed_transactions) > 0:
    high_failed_method = failed_payment_methods.index[0]
    if high_failed_method == "UPI":
        recommendation="Try the payment again using UPI or another payment method."
    elif high_failed_method=="Card":
        recommendation = "Ask the customer to check the card details or try another payment method."
    elif high_failed_method=="NetBanking":
        recommendation="Try NetBanking again or provide another payment option."
    elif high_failed_method == "Wallet":
        recommendation="Ask the customer to check the wallet balance or try another payment method."
    else:
        recommendation="Try some other available payment method or contact the customer for assistance."
    st.info(recommendation)
else:
    st.success("No failed payments need attention.")