from config import *

x, conn = connect_sqlite("recent_capitol")
x.execute('')
x.execute("PRAGMA table_info('locations')")
for row in x.fetchall():
    print(row)
conn.commit()
conn.close()