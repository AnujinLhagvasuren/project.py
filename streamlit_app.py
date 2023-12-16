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

price_dict = {
    'AAR': "Buy price is 2700 tugruk and Sale price is 3160 tugruks",
}

# Assume stock_dropdown is a variable with the selected stock
stock_dropdown = 'AAR'  # You should replace this with your actual logic for selecting a stock

# Use get method to retrieve the value from price_dict, and handle the case where it's not found
selected = price_dict.get(stock_dropdown, f"No information available for {stock_dropdown}")
st.write(f"Price info {stock_dropdown}:", selected)



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
    #showing chosen symbol with chosen stock on same axis



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

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(
    b, key="echarts"
)  # Add key argument to not remount component at every Streamlit run
st.button("Randomize data")

from pyecharts import options as opts
from streamlit_echarts import st_pyecharts
import random

# Sample data for multiple stocks
stock_info_dict = {
    'AAR': {"buy_price": 2700, "sell_price": 3160},
    # Add more stocks and their information here
}

# Sidebar for single stock selection
symbol_options = list(stock_info_dict.keys())
symbol = st.sidebar.selectbox("Select Stock Symbol", symbol_options)
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))

# Display selected stock information
st.write(f"## {symbol} Stock Information")
st.write(f"Buy Price: {stock_info_dict[symbol]['buy_price']}")
st.write(f"Sell Price: {stock_info_dict[symbol]['sell_price']}")

# ... (previous code)

# Bar chart using pyecharts
b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(
    b, key="echarts"
)  # Add key argument to not remount component at every Streamlit run

# ... (previous code)

# Plot stock closing price using Plotly Express
st.write(f"## {symbol} Closing Price Chart")
closing_price_chart = px.line(stock_df, x=stock_df.index, y="Close", title=f"{symbol} Closing Price")
st.plotly_chart(closing_price_chart)

# Button to randomize data
if st.button("Randomize Data"):
    # For demonstration purposes, randomly update the stock data
    stock_df["Close"] = random.sample(range(100), len(stock_df))
    st.success("Data randomized successfully!")

# ... (remaining code)

