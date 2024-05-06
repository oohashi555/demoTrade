import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS USER_ACCOUNT ( \
		USER_ID INTEGER PRIMARY KEY, \
		AMOUNT INTEGER NOT NULL)')

def select_amount(con, data):
    return con.execute('SELECT AMOUNT FROM USER_ACCOUNT WHERE USER_ID = ?', [data['user_id']]).fetchall()[0][0]

def insert(con,data):
	con.execute('INSERT INTO USER_ACCOUNT (USER_ID, AMOUNT) VALUES(?, ?)', [data['user_id'], data['amount']])

def delete(con,data):
    con.execute('DELETE FROM USER_ACCOUNT WHERE USER_ID = ?',[data['user_id']])

def update(con,data):
    con.execute('UPDATE USER_ACCOUNT SET AMOUNT = ? WHERE USER_ID = ?',[data['amount'], data['user_id']])
