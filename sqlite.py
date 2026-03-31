from config import *
import sqlite3 as sql

conn = sql.connect(f'test.db')
x = conn.cursor()

x.execute('select "index", country from test')
print(x.fetchall())

conn.close()