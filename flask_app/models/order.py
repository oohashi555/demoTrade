import sqlite3
from flask_app import app
import flask_app.db.position as pos

def select_position_list(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        position_list = pos.select_position_list(con, data)
    finally:
        con.close()
    return position_list

def order(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        data['order_price'] = 0
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
        pos.kessai(con,data)
        position_list = pos.select_position_list(con, data)
        con.commit()
        return position_list
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()
