from config import *

file_name = 'recent_capitol_original'
if os.path.exists(f'./dbs/{file_name}.db'): os.remove(f'./dbs/{file_name}.db')

x, conn = connect_sqlite(file_name)
df = get_df(file_name)

with open(f'{file_name}.sql', "r") as f:
    script = f.read()

conn.executescript(script)

x.execute("PRAGMA foreign_keys = ON")
clear_db(x)
get_tables(x)

for table in x.fetchall():
    table = table[0]
    get_pragma(x, table)
    cols = []
    ids = []

    for col in x.fetchall():
        col = col[1]
        if (col[-3:] == '_id'): 
            if (col[:-3] != table): ids.append(col[:-3])
        else: cols.append(col)

    if table == 'locations':
        dfx = cut_df(df, cols)
        dfx = dfx.drop_duplicates()
        dfx.to_sql(table, conn, if_exists='append', index = False)
        loc_map = pd.read_sql_query('SELECT locations_id, country, location_name, latitude, longitude, timezone FROM locations', conn)
        loc_cols = cols
    
    elif table == 'weather_observations':
        dfx = cut_df(df, loc_cols + cols)
        dfx = dfx.merge(loc_map, on=loc_cols, how='left')
        if dfx["locations_id"].isna().any(): raise ValueError("Some weather rows did not get a locations_id")
        dfx = dfx[["locations_id"] + cols].drop_duplicates(subset=["locations_id", "last_updated_epoch"])
        dfx.to_sql(table, conn, if_exists='append', index = False)
        observations_map = pd.read_sql_query('SELECT weather_observations_id, locations_id, last_updated_epoch FROM weather_observations', conn)
    
    else:
        dfx = cut_df(df, loc_cols + ['last_updated_epoch'] + cols)
        dfx = dfx.merge(loc_map, on=loc_cols, how='left').merge(observations_map, on=['locations_id', 'last_updated_epoch'], how='left')
        if dfx["weather_observations_id"].isna().any(): raise ValueError("Some rows did not get a weather_observations_id")
        dfx = dfx[['weather_observations_id'] + cols].drop_duplicates(subset = ['weather_observations_id'])
        dfx.to_sql(table, conn, if_exists='append', index=False)

summarize_db(conn, 1)
conn.commit()
conn.close()