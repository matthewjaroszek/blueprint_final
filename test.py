from config import *

db = 'recent_capitol_original'
x, conn = connect_sqlite(db)
dfo = get_df(db)
summarize_db(conn, 5)

conn.close