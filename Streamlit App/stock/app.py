import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write('''
# Simple Stock Price App
         Shown are the stock closing price and volume of GoJek

''')

#define the ticker symbol
tickerSymbol = 'GOTO.JK'

#get data on ticker 
tickerData = yf.Ticker(tickerSymbol)

today=datetime.date.today()
year_5 = today.year - 5

#date input
startdate = st.date_input("Start Date", datetime.date(year_5,1,1))
enddate = st.date_input('End Date',datetime.date.today())
#get the historical price for this ticker
tickerDF = tickerData.history(period='id', start= startdate, end=enddate)

#open high low close volume dividends stock splits
st.write('''
## Closing Price
         ''')
st.line_chart(tickerDF.Close)

st.write('''
## Volume Price
         ''')
st.line_chart(tickerDF.Volume)