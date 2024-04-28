import sqlite3
from flask_app import app
import flask_app.db.user_info as user

def select():
    con = sqlite3.connect(app.config['DATABASE'])
    user_list = user.select_all(con)
    con.close()
    return user_list

def regist(data):
    con = sqlite3.connect(app.config['DATABASE'])
    user_list = user.insert(con,data)
    con.commit()
    con.close()

def update(data):
    con = sqlite3.connect(app.config['DATABASE'])
    user_list = user.update(con,data)
    con.commit()
    con.close()

def delete(data):
    con = sqlite3.connect(app.config['DATABASE'])
    user_list = user.delete(con,data)
    con.commit()
    con.close()
