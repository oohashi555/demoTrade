from flask import Flask
app = Flask(__name__)
app.config.from_object('flask_app.config')

import flask_app.views.login
import pandas as pd
import sqlite3
import flask_app.db.ticker_info as ticker

# DBコネクション取得
con = sqlite3.connect(app.config['DATABASE'])

# 証券コードテーブル作成
ticker.create_table(con)

if ticker.count(con) == 0:
    ticker.create_index(con)
    excel = pd.read_excel('flask_app/data_j.xls')
    for i in range(len(excel)):
        ticker.insert(con,\
                        [excel.iloc[i, 1],\
                        excel.iloc[i, 2],\
                        excel.iloc[i, 3],\
                        str(excel.iloc[i, 4]).replace('-',''),\
                        str(excel.iloc[i, 5]).replace('-','')])
    con.commit()

con.close()
