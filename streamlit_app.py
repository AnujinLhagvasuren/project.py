import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("project1data.csv")
st.dataframe(df)



# Function to fetch stock data using yfinance
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Sidebar with user input
st.sidebar.header("Stock Dashboard")
symbol = st.sidebar.text_input("Enter Stock Symbol:", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))

# Fetch stock data
try:
    stock_df = get_stock_data(symbol, start_date, end_date)

    # Display stock data
    st.write(f"## {symbol} Stock Data")
    st.dataframe(stock_df.head())

    # Plot stock closing price
    st.write(f"## {symbol} Closing Price Chart")
    fig = px.line(stock_df, x=stock_df.index, y="Close", title=f"{symbol} Closing Price")
    st.plotly_chart(fig)

    # Interactive widgets
    st.write("## Interactive Widgets")
    selected_feature = st.selectbox("Select Feature:", stock_df.columns)
    st.line_chart(stock_df[selected_feature])

    # Additional analysis or visualizations can be added here

except Exception as e:
    st.error(f"Error fetching stock data: {e}")
