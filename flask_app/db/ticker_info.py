import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS TICKER_INFO ( \
		TICKER_CODE TEXT PRIMARY KEY, \
		NAME TEXT NOT NULL)')

def count(con):
	return con.execute('SELECT COUNT(*) CNT FROM TICKER_INFO').fetchall()[0][0]

def insert(con,data):
	con.execute('INSERT INTO TICKER_INFO VALUES(?, ?)', [data[0], data[1]])
	