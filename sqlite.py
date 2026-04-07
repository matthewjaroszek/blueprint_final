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

    dfx = cut_df(df, cols)

    if table == 'locations':
        dfx = dfx.drop_duplicates()
        dfx.to_sql(table, conn, if_exists='append', index = False)
        print(get_pragmas(x)[0])
        summarize_db(conn)
        #location_map = pd.read_sql_query('SELECT locations_id, country, location_name, latitude, longitude, timezone FROM locations', conn)
        #summarize_df(location_map)

conn.commit()
conn.close()