import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS POSITION ( \
		POSITION_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		USER_ID INTEGER NOT NULL, \
		TICKER_CODE TEXT NOT NULL, \
		BUYSELL TEXT NOT NULL, \
		ORDER_PRICE INTEGER NOT NULL, \
		KESSAI_PRICE INTEGER NOT NULL, \
		LOT INTEGER NOT NULL, \
      	ACTIVE_FLAG INTEGER DEFAULT 0 NOT NULL)')

def create_index(con):
	con.execute('CREATE INDEX IF NOT EXISTS POSITION_INDEX ON POSITION(USER_ID)')

def select_position_list(con, data):
    return con.execute('SELECT POS.POSITION_ID, POS.TICKER_CODE, POS.BUYSELL, POS.ORDER_PRICE, POS.KESSAI_PRICE, POS.LOT, TIC.NAME FROM POSITION POS \
						INNER JOIN TICKER_INFO TIC ON POS.TICKER_CODE = TIC.TICKER_CODE \
        				WHERE POS.USER_ID = ? AND POS.ACTIVE_FLAG = 0', [data['user_id']]).fetchall()

def select_position_history(con, data):
    return con.execute('SELECT POS.POSITION_ID, POS.TICKER_CODE, POS.BUYSELL, POS.ORDER_PRICE, POS.KESSAI_PRICE, POS.LOT, TIC.NAME FROM POSITION POS \
						INNER JOIN TICKER_INFO TIC ON POS.TICKER_CODE = TIC.TICKER_CODE \
        				WHERE POS.USER_ID = ? AND POS.ACTIVE_FLAG = 1', [data['user_id']]).fetchall()

def insert(con,data):
	con.execute('INSERT INTO POSITION (USER_ID, TICKER_CODE, BUYSELL, ORDER_PRICE, KESSAI_PRICE, LOT) VALUES(?, ?, ?, ?, ?, ?)', \
     			[data['user_id'], data['ticker_code'], data['buysell'], data['order_price'], data['kessai_price'], data['lot']])

def delete(con,data):
    con.execute('DELETE FROM POSITION WHERE USER_ID = ?',[data['user_id']])

def kessai(con,data):
    con.execute('UPDATE POSITION SET KESSAI_PRICE = ?, ACTIVE_FLAG = ? WHERE POSITION_ID = ?',[data['kessai_price'], 1, data['position_id']])
