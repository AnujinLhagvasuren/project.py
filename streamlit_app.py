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

symbol_options = [
    "AAR", "AARD", "ABH", "ACL", "ADB", "ADL", "ADU", "AHH", "AIC", "ALA", "ALD", "ALI", "AMT", 
    "AOI", "APU", "ARJ", "ATR", "AZH", "BAJ", "BAN", "BAZ", "BBD", "BDL", "BDS", "BEU", "BHG", 
    "BHL", "BHR", "BLC", "BLG", "BNG", "BODI", "BOE", "BOGD", "BOR", "BRC", "BSKY", "BTG", "BUK", 
    "CHR", "CND", "CNF", "CUMN", "DAH", "DAR", "DAZ", "DES", "DHU", "DLH", "DMA", "DSS", "DZG", 
    "EAZ", "ECV", "EER", "ERDN", "ERS", "ETR", "GAZR", "GFG", "GHC", "GLMT", "GNR", "GOV", "GOV", 
    "GTJ", "GTL", "GUR", "HAM", "HBO", "HBT", "HBZ", "HGN", "HHN", "HHS", "HJL", "HML", "HRD", 
    "HRL", "HRM", "HSG", "HSR", "HSX", "HTS", "HUN", "HUV", "HVL", "IBA", "INT", "INV", "ITLS", 
    "JGL", "JGV", "JLT", "JTB", "KEK", "KHAN", "LEND", "MBG", "MBW", "MCH", "MDIC", "MDR", "MDZ", 
    "MFC", "MFG", "MIB", "MIE", "MIK", "MLG", "MMX", "MNB", "MNDL", "MNG", "MNH", "MNP", "MNS", 
    "MOG", "MRX", "MSC", "MSE", "MSH", "MUDX", "MVO", "NEH", "NKT", "NOG", "NRS", "NXE", "OLL", 
    "ONH", "ORD", "RMC", "SBM", "SDT", "SEND", "SES", "SHG", "SHV", "SIL", "SOH", "SOR", "SSG", 
    "SUN", "SUU", "SVR", "TAH", "TAL", "TAS", "TAV", "TCK", "TDB", "TEE", "TEX", "TGS", "TLP", 
    "TMZ", "TNGR", "TSA", "TTL", "TTL", "TUM", "TUS", "TVL", "TVT", "UBH", "UID", "ULZ", "UNS", 
    "UYN", "VIK", "XAC", "XOC", "BEND", "BGFI"]


symbol = st.sidebar.selectbox("Select Stock Symbol", symbol_options)
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))




import streamlit as st

def main():
    st.title("Dashboard")

    # Sample data
    buy_price = [2700.00, 3017.00]
    sell_price = [3160.00, 3031.00]
    industry_average = [375583500.00, 86701216890.00]

    # Display buy price
    st.header("Buy Price")
    st.write(f"First buy price: {buy_price[0]}")
    st.write(f"Second buy price: {buy_price[1]}")

    # Display sell price
    st.header("Sell Price")
    st.write(f"First sell price: {sell_price[0]}")
    st.write(f"Second sell price: {sell_price[1]}")

    # Display industry average
    st.header("Industry Average")
    st.write(f"First industry average: {industry_average[0]}")
    st.write(f"Second industry average: {industry_average[1]}")

if __name__ == "__main__":
    main()


# Fetch stock data
try:
    stock_df = get_stock_data(symbol, start_date, end_date)

    # Display stock data
    st.write(f"## {symbol} Stock Data")
    st.dataframe(stock_df.head())

    # Plot stock closing price
    st.write(f"## {symbol} Buy Price Chart")
    fig = px.line(stock_df, x=stock_df.index, y="Open", title=f"{symbol} Buy Price")
    st.plotly_chart(fig)

    # Interactive widgets
    st.write("## Interactive Widgets")
    selected_feature = st.selectbox("Select Feature:", stock_df.columns)
    st.line_chart(stock_df[selected_feature])

    # Additional analysis or visualizations can be added here

except Exception as e:
    st.error(f"Error fetching stock data: {e}")
    
# Sidebar for multiple stock selection
selected_stocks = st.sidebar.multiselect("Select Stocks", [
    "АВТО ЗАМ", "АРД САНХҮҮГИЙН НЭГДЭЛ", "АР БАЯНХАНГАЙ", 
    "ТЭЭВЭР-АЧЛАЛ", "АРД КРЕДИТ ББСБ ХК", "АДУУН ЧУЛУУН", "ХӨВСГӨЛ АЛТАН ДУУЛГА", 
    "ХОРИН ХОЁРДУГААР БААЗ", "АРД ДААТГАЛ ХК", "АЛТАЙ НЭГДЭЛ", "АЗЫК", "СТАНДАРТ НООС", 
    "ЭРДЭНЭС СОЛЬЮШИНС", "АВТО ИМПЕКС", "АПУ", "АРВИЖИХ", "АТАР-ӨРГӨӨ", "АЛТАЙН ЗАМ", 
    "БАЯЛАГ-СҮМБЭР", "БАГАНУУР", "ЛЮКС ЗАНАДУ ГРУПП", "СТАНДАРТ ПРОПЕРТИ ГРУПП", 
    "МОГОЙН ГОЛ", "БИ ДИ СЕК", "БЭРХ УУЛ", "БӨХӨГ", "БӨӨНИЙ ХУДАЛДАА ХК", "БИНСЭ ХК", 
    "БҮТЭЭЛЧ ҮЙЛС", "ЗАВХАН БАЯЛАГ", "БАЯНГОЛ ЗОЧИД БУУДАЛ", "Бодь Даатгал ХК", 
    "ЭРЧИМ БАЯН ӨЛГИЙ", "БОГД БАНК", "БОРНУУР", "БАРИЛГА КОРПОРАЦИ", "БЛЮСКАЙ СЕКЬЮРИТИЗ", 
    "БАЯНТЭЭГ", "УБ-БҮК", "УВС ЧАЦАРГАНА", "АСБИ", "Крипто Үндэстэн ХК", 
    "CЭНТРАЛ ЭКСПРЕСС СИ ВИ ЭС", "ДАРХАН ХӨВӨН", "ДАРХАН ГУРИЛ ТЭЖЭЭЛ", "ДОРНОД АВТО ЗАМ", 
    "ДОРНОД ХУДАЛДАА", "ДАРХАН ХҮНС", "ЭМ ЭН ДИ", "ДЭВШИЛ МАНДАЛ", 
    "ДАРХАН СЭЛЭНГИЙН ЦАХИЛГААН ДУЛААН СҮЛЖЭЭ", "ДАРХАН ЗОЧИД БУУДАЛ", "ЭРДЭНЭТ АВТО ЗАМ", 
    "ЭРЭЭНЦАВ", "АРИГ ГАЛ", "ЭРДЭНЭ РЕСУРС ДЕВЕЛОПМЕНТ КОРПОРЭЙШН ХК", "МОНГОЛ АЛТ", 
    "Э-ТРАНС ЛОЖИСТИКС", "ГАЗАР ШИМ ҮЙЛДВЭР", "И ЭС ЖИ ФАЙНАНС", "ГАН ХИЙЦ", "ГОЛОМТ БАНК", 
    "ГОНИР", "ГОВЬ", "ГОВЬ", "ГУРИЛ ТЭЖЭЭЛ БУЛГАН", "ГУТАЛ", "ГУРИЛ", 
    "МОНГОЛЫН ХӨГЖИЛ ҮНДЭСНИЙ НЭГДЭЛ", "ХАЙ БИ ОЙЛ", "ХӨНГӨН БЕТОН", "ХҮННҮ МЕНЕЖМЕНТ", 
    "ХӨХ ГАН", "ХАРХОРИН", "ХӨВСГӨЛ ХҮНС", "ОРХОН ХӨГЖИЛ", "ГЛОБАЛ МОНГОЛИА ХОЛДИНГС", 
    "ХҮРД", "ХЭРЛЭН ХИВС", "ГЕРМЕС ЦЕНТР", "ХӨСӨГ ТРЕЙД", "ХАСУ-МАНДАЛ", "ХИШИГ УУЛ", 
    "ЦЕМЕНТ ШОХОЙ ХК", "УВС ХҮНС", "ХӨВСГӨЛ ГЕОЛОГИ", "ХӨВСГӨЛ", "ИХ БАРИЛГА", 
    "ИНГЭТТОЛГОЙ", "Инвескор ББСБ", "АЙТҮҮЛС", "ГОВИЙН ӨНДӨР", "ЖУУЛЧИН ГОВЬ", 
    "НОГООН ХӨГЖИЛ ҮНДЭСНИЙ НЭГДЭЛ", "ЖЕНКО ТУР БЮРО", "МОНГОЛ КЕРАМИК", "ХААН БАНК", 
    "ЛЭНДМН ББСБ ХК", "БУЛИГААР", "МОНГОЛ БАЗАЛЬТ ХК", "МОНГОЛЫН ЦАХИЛГААН ХОЛБОО", 
    "МОНГОЛ ДААТГАЛ", "ФРОНТИЕР ЛЭНД ГРУПП", "МОНГОЛ ДИЗЕЛЬ", "МОНОС ХҮНС", 
    "Мандал Ирээдүйн Өсөлт", "МОНИНЖБАР", "МАТЕРИАЛИМПЕКС", "МИК ХОЛДИНГ", 
    "МОНЛОЖИСТИКС ХОЛДИНГ", "МАХИМПЕКС", "МОН НАБ", "МАНДАЛ ДААТГАЛ", "МАНДАЛ ГОВЬ ИМПЭКС", 
    "МОНГОЛ НЭХМЭЛ", "МОНГОЛ ШУУДАН ХК", "МОННООС", "МОНГЕО", "MEPEKC", "МОНГОЛ СЕКЮРИТИЕС", 
    "МОНГОЛЫН ХӨРӨНГИЙН БИРЖ", "МОНГОЛ ШИЛТГЭЭН", "МҮДИКС", "МОНГОЛ ШЕВРО", "ДАРХАН НЭХИЙ", 
    "НАКО ТҮЛШ", "АЧИТ АЛКАБЫ", "ШИНЭСТ", "НЭХЭЭСГҮЙ ЭДЛЭЛ", "ОЛЛОО", "ӨНДӨРХААН", 
    "ОРХОНДАЛАЙ", "РЕМИКОН", "ТӨРИЙН БАНК", "ХОТ ДЕВЕЛОПМЕНТ", "СЭНДЛИ ББСБ", "СЭЛЭНГЭ СҮРЭГ", 
    "ШАРЫН ГОЛ", "ШИВЭЭ ОВОО", "СИЛИКАТ", "ЖИДАКС", "СОР", "СОНСГОЛОН БАРМАТ", 
    "ЕВРОАЗИА КАПИТАЛ ХОЛДИНГ", "СҮҮ", "ЭРДЭНЭТ СУВРАГА", "ТАХЬ-КО", "ТАЛЫН ГАЛ", "ЭРДЭНЭТ ХҮНС", 
    "ТАВ", "ТАЛХ ЧИХЭР", "ХУДАЛДАА ХӨГЖЛИЙН БАНК", "ТЭЭВЭР ДАРХАН", "ТЕХНИК ИМПОРТ", 
    "НОМИН ХИШИГ", "ТУЛПАР", "ТӨМРИЙН ЗАВОД", "Тэнгэрлиг медиа групп ХК", "ЦАГААНТОЛГОЙ", 
    "ТАВАН ТОЛГОЙ", "ТАВАН ТОЛГОЙ", "ТҮМЭН ШУВУУТ", "ТҮШИГ УУЛ", "ТАВИЛГА", "ХАР ТАРВАГАТАЙ", 
    "УЛААНБААТАР ХИВС", "УЛСЫН ИХ ДЭЛГҮҮР", "ӨЛЗИЙ- ДУНДГОВЬ", "УЛААНСАН", "МОНГОЛ САВХИ", 
    "ТАНДЭМ ИНВЭСТ ББСБ", "ХАС БАНК", "ҮНДЭСНИЙ ХУВЬЧЛАЛЫН САН", "BEND-BD-30/07/24-C0039-19.2", 
    "BGFI-BD-30/06/25-C0046-18.5"])



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

# Calculate Bollinger Bands
stock_df['Rolling Mean'] = stock_df['Close'].rolling(window=20).mean()
stock_df['Upper Band'] = stock_df['Rolling Mean'] + 2 * stock_df['Close'].rolling(window=20).std()
stock_df['Lower Band'] = stock_df['Rolling Mean'] - 2 * stock_df['Close'].rolling(window=20).std()

# Display Bollinger Bands chart
st.write("## Bollinger Bands Chart")
fig_bollinger = px.line(stock_df, x=stock_df.index, y=["Close", "Upper Band", "Lower Band"], title=f"{symbol} Bollinger Bands")
st.plotly_chart(fig_bollinger)

# Calculate MACD
stock_df['ShortEMA'] = stock_df['Close'].ewm(span=12, adjust=False).mean()
stock_df['LongEMA'] = stock_df['Close'].ewm(span=26, adjust=False).mean()
stock_df['MACD'] = stock_df['ShortEMA'] - stock_df['LongEMA']
stock_df['Signal Line'] = stock_df['MACD'].ewm(span=9, adjust=False).mean()

# Display MACD chart
st.write("## MACD Chart")
fig_macd = px.line(stock_df, x=stock_df.index, y=["MACD", "Signal Line"], title=f"{symbol} MACD")
st.plotly_chart(fig_macd)

import requests

# Function to fetch financial news
def get_financial_news(symbol):
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey=YOUR_NEWS_API_KEY"
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

# Fetch financial news for the selected stock
news_articles = get_financial_news(symbol)

# Display financial news
st.write("## Financial News")
for article in news_articles:
    st.write(f"### {article['title']}")
    st.write(article['description'])
    st.write(f"Source: {article['source']['name']}")
    st.write(f"Published At: {article['publishedAt']}")
    st.write("---")

