import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS POSITION ( \
		POSITION_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		USER_ID INTEGER NOT NULL, \
		TICKER_CODE TEXT NOT NULL, \
		BUYSELL TEXT NOT NULL, \
		PRICE INTEGER NOT NULL, \
		LOT INTEGER NOT NULL, \
      	ACTIVE_FLAG INTEGER DEFAULT 0 NOT NULL)')

def create_index(con):
	con.execute('CREATE INDEX IF NOT EXISTS POSITION_INDEX ON POSITION(USER_ID)')

def select_position_list(con, data):
    return con.execute('SELECT POSITION_ID, TICKER_CODE, BUYSELL, PRICE, LOT FROM POSITION WHERE USER_ID = ? AND ACTIVE_FLAG = 0', [data['user_id']]).fetchall()

def insert(con,data):
	con.execute('INSERT INTO POSITION (USER_ID, TICKER_CODE, BUYSELL, PRICE, LOT) VALUES(?, ?, ?, ?, ?)', \
     			[data['user_id'], data['ticker_code'], data['buysell'], data['price'], data['lot']])

def delete(con,data):
    con.execute('DELETE FROM POSITION WHERE USER_ID = ?',[data['user_id']])

def kessai(con,data):
    con.execute('UPDATE POSITION SET ACTIVE_FLAG = ? WHERE POSITION_ID = ?',[1, data['position_id']])
