import sqlite3

def create_table(con):
	con.execute( \
		'CREATE TABLE IF NOT EXISTS USER_INFO ( \
		ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		NAME TEXT, \
		PASSWORD TEXT )')
	
def check_password(con,data):
	return con.execute('SELECT COUNT(*) CNT FROM USER_INFO WHERE ID = ?, PASSWORD = ?',[data['id'], data['password']]).fetchall()[0][0] == 1

def select_all(con):
    return con.execute('SELECT ID, NAME FROM USER_INFO').fetchall()

def insert(con,data):
	con.execute('INSERT INTO USER_INFO (NAME, PASSWORD) VALUES(?, ?)', [data['name'], data['password']])

def delete(con,data):
    con.execute('DELETE FROM USER_INFO WHERE ID = ?',[data['id']])

def update(con,data):
    con.execute('UPDATE USER_INFO SET NAME = ?, PASSWORD = ? WHERE ID = ?',[data['name'], data['password'], data['id']])
