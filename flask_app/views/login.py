from flask_app import app
from flask import render_template
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime
import mplfinance as mf

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    start = datetime.date(datetime.datetime.now().year - 1, datetime.datetime.now().month, datetime.datetime.now().day)
    end = datetime.datetime.now()
    
    #ticker = yf.Ticker('GOOGL').info
    #price = ticker['currentPrice']

    ticker = '9984.T'
    #history = yf.download(ticker, start, end)
    #chart = mf.plot(history)
    
    #yf.pdr_override()
    #df = pdr.get_data_yahoo(ticker, start, end)
    
    tickerInfo = yf.Ticker(ticker)
    return render_template('top.html', price = tickerInfo.history(period='max'))