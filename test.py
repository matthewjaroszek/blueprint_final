from config import *

x, conn = connect_sqlite('recent_capitol_original')
dfo = get_df('recent_capitol_original')

#rename_update('recent_capitol_original', 'air_quality_pm25', 'air_quality_pm2_5')

summarize_df(get_df('recent_capitol_original'))
x.execute(f'PRAGMA table_info(air_quality_observations)')
print(x.fetchall())
summarize_db(conn, 5)
conn.close