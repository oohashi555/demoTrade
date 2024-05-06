import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS USER_INFO ( \
		USER_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		NAME TEXT NOT NULL, \
		PASSWORD TEXT NOT NULL )')
	
def check_password(con,data):
	return con.execute('SELECT COUNT(*) CNT FROM USER_INFO WHERE USER_ID = ?, PASSWORD = ?',[data['user_id'], data['password']]).fetchall()[0][0] == 1

def select_all(con):
    return con.execute('SELECT USER_ID, NAME FROM USER_INFO').fetchall()

def select_max_user_id(con):
    return con.execute('SELECT MAX(USER_ID) FROM USER_INFO').fetchall()[0][0]

def insert(con,data):
	con.execute('INSERT INTO USER_INFO (NAME, PASSWORD) VALUES(?, ?)', [data['name'], data['password']])

def delete(con,data):
    con.execute('DELETE FROM USER_INFO WHERE USER_ID = ?',[data['user_id']])

def update(con,data):
    con.execute('UPDATE USER_INFO SET NAME = ?, PASSWORD = ? WHERE USER_ID = ?',[data['name'], data['password'], data['user_id']])
