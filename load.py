from config import *

n = 50
df = getdf('rc').head(n)
df.to_csv(gzs['rc'], index = False)
df = getdf('dc').head(n)
df.to_csv(gzs['dc'], index = False)

for gz in gzs:
    df = getdf(gz)
    conn = sql.connect(f'./dbs/{gz}.db')
    df.to_sql(f'{gz}', conn, if_exists='replace')
    x = conn.cursor()
    x.execute(f'DROP INDEX IF EXISTS ix_{gz}_index')
    x.execute(f'ALTER TABLE {gz} DROP COLUMN "index"')
    conn.commit()
    conn.close()

if len(sys.argv) >= 2:
    if (int)(sys.argv[1]) == 1:
        summarize({'rc', 'dc'}, 5, 0)
    if len(sys.argv) >= 3 and (int)(sys.argv[2]) == 1:
        run_sql({'rc', 'dc'}, "PRAGMA table_info({})", True)