import streamlit as st
from data_ingestion import fetch_financials, fetch_news

def check_loan_eligibility(financials):
    debt_to_equity = financials.get("debtToEquity")
    profit_margins = financials.get("profitMargins")
    revenue_growth = financials.get("revenueGrowth")
    current_price = financials.get("currentPrice")

    if None in (debt_to_equity, profit_margins, revenue_growth, current_price):
        return "Insufficient data", 0

    eligible = (
        debt_to_equity < 200 and
        profit_margins > 0.1 and
        revenue_growth > 0
    )

    if eligible:
        if debt_to_equity < 100 and profit_margins > 0.2 and revenue_growth > 0.05:
            percent = 80
        else:
            percent = 60
        return "Eligible", percent
    else:
        return "Not Eligible", 0

st.title("Credit Intelligence Platform")

company = st.text_input("Enter Company Name (e.g., Apple):", "Apple")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")

if st.button("Get Data"):
    st.subheader("Financial Data")
    financials = fetch_financials(ticker)
    st.json(financials)

    st.subheader("Loan Eligibility")
    status, percent = check_loan_eligibility(financials)
    st.write(f"Loan Status: **{status}**")
    if percent > 0:
        st.write(f"Maximum Loan Percentage: **{percent}%** of current price")

    st.subheader("Recent News")
    news = fetch_news(company)
    if news:
        for article in news:
            st.write(article)
    else:
        st.write("No news found.")