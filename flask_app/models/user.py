import sqlite3
from flask_app import app
import flask_app.db.user_info as user
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
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

def update(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user.update(con,data)
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

def delete(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        user.delete(con, data)
        pos.delete(con, data)
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

def check_password(data):
    con = sqlite3.connect(app.config['DATABASE'])
    try:
        ok = user.check_password(con, data)
    finally:
        con.close()
    return ok
