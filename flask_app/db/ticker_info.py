import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS TICKER_INFO ( \
		CODE TEXT PRIMARY KEY, \
		NAME TEXT NOT NULL, \
		MARKET TEXT , \
		INDUSTRY_CODE TEXT , \
		INDUSTRY TEXT )')

def create_index(con):
	con.execute('CREATE INDEX IF NOT EXISTS TICKER_INFO_INDEX ON TICKER_INFO(NAME, MARKET, INDUSTRY_CODE)')
	
def count(con):
	return con.execute('SELECT COUNT(*) CNT FROM TICKER_INFO').fetchall()[0][0]

def insert(con,data):
	con.execute('INSERT INTO TICKER_INFO VALUES(?, ?, ?, ?, ?)', [data[0], data[1], data[2], data[3], data[4]])
	