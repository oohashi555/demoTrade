import sqlite3
from flask_app import app
import flask_app.db.user_info as user
import flask_app.db.user_account as user_ac
import flask_app.db.position as pos

def select():
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user_list = user.select_all(con)
    finally:
        con.close()
    return user_list

def regist(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user.insert(con,data)
        user_id = user.select_max_user_id(con)
        user_ac.insert(con, {'user_id': user_id, 'amount': 0})
        con.commit()
    except Exception:
        con.rollback()
    finally:
        con.close()

def update(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user.update(con,data)
        con.commit()
    except Exception:
        con.rollback()
    finally:
        con.close()

def delete(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user.delete(con, data)
        user_ac.delete(con, data)
        pos.delete(con, data)
        con.commit()
    except Exception:
        con.rollback()
    finally:
        con.close()
