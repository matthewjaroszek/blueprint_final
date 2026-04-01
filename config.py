import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3 as sql
import psycopg2 as pgs
import sys, argparse

load_dotenv()
sql_url = os.getenv('sql_url')



def copy_gz(original_name, copy_name):
    copy = pd.read_csv(f'./gzs/{original_name}.gz')
    copy.to_csv(f'./gzs/{copy_name}.gz', index = False)

def get_df(file_name):
    return pd.read_csv(f'./gzs/{file_name}.gz')
    
def summarize_df(df, rows = 5):
    print(f'{df.shape[0]} rows by {df.shape[1]} cols', '\n')
    cols = df.columns
    x = 0
    for col in cols:
        x += 1
        print(f'{col:^20}', end = "")
        if x >= 9:
            print("")
            x = 0
        else:
            print(" - ", end = "")
    print(df.head(rows), "\n")

def rename_col(df, old, new):
    df.rename(columns={old: new}, inplace = True)

def delete_col(df, col):
    df.drop(col, axis = 1, inplace = True)

def connect_sqlite(file_name):
    conn = sql.connect(f'./dbs/{file_name}.db')
    x = conn.cursor()
    return x, conn

def check_args(i):
    return len(sys.argv) > i and (int)(sys.argv[i]) == 1

def load_db(df, file_name):
    x, conn = connect_sqlite(file_name)
    df.to_sql(file_name, conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()

