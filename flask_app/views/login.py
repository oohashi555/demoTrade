from flask_app import app
from flask import render_template
import yfinance as yf
import datetime

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    
    ticker = '9984.T'
    
    history = yf.download(ticker,period = '1y', interval = '1wk')
    axes = history.axes[0]
    open = history.Open.values
    high = history.High.values
    low = history.Low.values
    close = history.Close.values
    
    return render_template('top.html', axes = axes, open = open, high = high, low = low, close = close)
