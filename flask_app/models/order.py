import sqlite3
from flask_app import app
import flask_app.db.position as pos
import yfinance as yf

def select_position_list(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        position_list = pos.select_position_list(con, data)
        history_list = pos.select_position_history(con, data)
    finally:
        con.close()
    return {'position': position_list, 'history': history_list}

def order(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        ticker = yf.download(data['ticker_code'],period = '1d', interval = '1m')
        data['order_price'] = round(ticker.Close.values[ticker.Close.size - 1])
        data['kessai_price'] = 0
        pos.insert(con,data)
        position_list = pos.select_position_list(con, data)
        con.commit()
        return position_list
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

def kessai(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        ticker = yf.download(data['ticker_code'],period = '1d', interval = '1m')
        data['kessai_price'] = round(ticker.Close.values[ticker.Close.size - 1])
        pos.kessai(con,data)
        position_list = pos.select_position_list(con, data)
        history_list = pos.select_position_history(con, data)
        con.commit()
        return {'position': position_list, 'history': history_list}
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()
