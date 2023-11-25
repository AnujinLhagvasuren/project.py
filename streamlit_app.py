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


# Sidebar for multiple stock selection
selected_stocks = st.sidebar.multiselect("Select Stocks", ["AAPL", "GOOGL", "MSFT"])

# Fetch stock data for selected stocks
stock_dfs = {}
for stock in selected_stocks:
    stock_dfs[stock] = get_stock_data(stock, start_date, end_date)

# Display multiple stock data
st.write("## Multiple Stock Data")
for stock, df in stock_dfs.items():
    st.write(f"### {stock} Stock Data")
    st.dataframe(df.head())

# Plot multiple stock closing prices
st.write("## Multiple Stock Closing Price Chart")
fig_multi = px.line()
for stock, df in stock_dfs.items():
    fig_multi.add_scatter(x=df.index, y=df["Close"], mode='lines', name=stock)

st.plotly_chart(fig_multi)

# Fetch stock data with additional parameters for candlestick chart
candlestick_df = yf.download(symbol, start=start_date, end=end_date, interval='1d')

# Display candlestick chart
st.write(f"## {symbol} Candlestick Chart")
fig_candlestick = px.candlestick(candlestick_df, x=candlestick_df.index, open='Open', high='High', low='Low', close='Close', title=f"{symbol} Candlestick Chart")
st.plotly_chart(fig_candlestick)

# Rolling average period
rolling_period = st.sidebar.slider("Select Rolling Average Period", min_value=1, max_value=30, value=10)

# Calculate rolling average
stock_df['Rolling Average'] = stock_df['Close'].rolling(window=rolling_period).mean()

# Display rolling average chart
st.write("## Rolling Average Chart")
fig_rolling_avg = px.line(stock_df, x=stock_df.index, y=["Close", "Rolling Average"], title=f"{symbol} Closing Price with Rolling Average")
st.plotly_chart(fig_rolling_avg)

# Calculate daily returns
stock_df['Daily Return'] = stock_df['Close'].pct_change()

# Display daily returns chart
st.write("## Daily Returns Chart")
fig_returns = px.line(stock_df, x=stock_df.index, y="Daily Return", title=f"{symbol} Daily Returns")
st.plotly_chart(fig_returns)

