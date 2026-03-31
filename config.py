import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3 as sql
import psycopg2 as pgs
import sys, argparse

print()
load_dotenv()
sql_url = os.getenv('sql_url')

gzs = {
    "rc" : "gzs/rc.gz",
    "dc" : "gzs/dc.gz",
    "trc" : "gzs/trc.gz",
    "tdc" : "gzs/tdc.gz",
}

dbs = {
    "rc" : "dbs/rc.db",
    "dc" : "dbs/dc.db",
    "trc" : "dbs/trc.db",
    "tdc" : "dbs/tdc.db",
}

def getdf(gz):
    return pd.read_csv(gzs[gz])

def summarize(gzs, r = 0, c = 0):
    if isinstance(gzs, str):
        print(f'{gzs}: ', end = "")
        summarize(getdf(gzs), r, c)
    
    elif isinstance(gzs, dict) or isinstance(gzs, set):
        for gz in gzs:
            summarize(gz, r, c)

    elif isinstance(gzs, pd.DataFrame):
        print(f'{gzs.shape[0]} x {gzs.shape[1]} ', '-'*185, '\n')
        cols = gzs.columns
        x = 0
        for col in cols:
            x += 1
            print(f'{col:^20}', end = "")
            if x >= 9:
                print("")
                x = 0
            else:
                print(" - ", end = "")
        print("\b\b  ")
        print()
        if (r*c > 0):
            print("", gzs.iloc[:r, :c], "\n")

def nc(gz, old, new):
    df = getdf(gz)
    df = df.rename(columns={old: new})
    df.to_csv(gzs[gz], index = False)

def drop(gz, col):
    df = getdf(gz)
    df = df.drop(col, axis = 1)
    df.to_csv(gzs[gz], index = False)
    return getdf(gz)

def print_sql(x, dbs, b = True):
    if (not b):
        return
    print(f"{dbs}", "-"*35, "\n")
    x = x.fetchall()
    for r in x:
        print(r)
    print()

def run_sql(dbs, ex, b = True):
    if (isinstance(dbs, str)):
        conn = sql.connect(f'./dbs/{dbs}.db')
        x = conn.cursor()
        x.execute(ex.format(dbs))
        print_sql(x, dbs, b)
        conn.close()
    
    elif isinstance(dbs, dict) or isinstance(dbs, set):
        for db in dbs:
            run_sql(db, ex, b)