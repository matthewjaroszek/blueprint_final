from config import *

n = 50
df = getdf('rc').head(n)
df.to_csv("trc.gz", index = False)
df = getdf('dc').head(n)
df.to_csv("tdc.gz", index = False)

for csv in csvs:
    df = getdf(csv)
    conn = sql.connect(f'{csv}.db')
    df.to_sql(f'{csv}', conn, if_exists='replace')
    x = conn.cursor()
    x.execute(f'DROP INDEX IF EXISTS ix_{csv}_index')
    x.execute(f'ALTER TABLE {csv} DROP COLUMN "index"')
    conn.commit()
    conn.close()

summarize({'rc', 'dc'}, 5, 0)
run_sql({'rc', 'dc'}, "PRAGMA table_info({})", True)