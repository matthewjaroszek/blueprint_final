from config import *

x, conn = connect_sqlite('recent_capitol')
dfo = get_df('recent_capitol_original')
summarize_df(dfo)
df_locations = dfo[["country", "city", "latitude", "longitude", "time_zone"]]
df_locations = df_locations.drop_duplicates()
df_locatoins = df_locations.sort_values(by="country")
df_locations.to_sql('locations', conn, if_exists = 'replace')

x.execute('SELECT * FROM locations')
for row in x.fetchall():
    print(row)
conn.commit()
conn.close

summarize_df(dfo)
