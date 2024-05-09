import pandas as pd
import sqlite3
import flask_app.db.ticker_info as ticker
import flask_app.db.user_info as user
import flask_app.db.position as pos
from flask_app import app

def create_db():
    # DBコネクション取得
    con = sqlite3.connect(app.config['DATABASE'])
    
    try:
        # ユーザ管理テーブル作成
        user.create_table(con)
        
        # ポジションテーブル作成
        pos.create_table(con)
        pos.create_index(con)
        
        # 証券コードテーブル作成
        ticker.create_table(con)
        
        # 証券コードデータの登録
        if ticker.count(con) == 0:
            excel = pd.read_excel('flask_app/data_i.xls')
            for i in range(len(excel)):
                ticker.insert(con,\
                                [excel.iloc[i, 0],\
                                excel.iloc[i, 1]])
            con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()
