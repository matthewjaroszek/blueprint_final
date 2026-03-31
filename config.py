import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3 as sql
import psycopg2 as pgs

load_dotenv()
print()

csvs = {
    "rc" : "rc.gz",
    "dc" : "dc.gz",
    "trc" : "trc.gz",
    "tdc" : "tdc.gz",
}

def getdf(csv):
    return pd.read_csv(csvs[csv])

def summarize(csvs, r = 0, c = 0):
    if isinstance(csvs, str):
        print(f'{csvs}: ', end = "")
        summarize(getdf(csvs), r, c)
    
    elif isinstance(csvs, dict) or isinstance(csvs, set):
        for csv in csvs:
            summarize(csv, r, c)

    elif isinstance(csvs, pd.DataFrame):
        print(f'{csvs.shape[0]} x {csvs.shape[1]} ', '-'*185, '\n')
        cols = csvs.columns
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
            print("", csvs.iloc[:r, :c], "\n")

def nc(csv, old, new):
    df = getdf(csv)
    df = df.rename(columns={old: new})
    df.to_csv(csvs[csv], index = False)

def drop(csv, col):
    df = getdf(csv)
    df = df.drop(col, axis = 1)
    df.to_csv(csvs[csv], index = False)
    return getdf(csv)

def print_sql(x, csvs, b = True):
    if (not b):
        return
    print(f"{csvs}", "-"*35, "\n")
    x = x.fetchall()
    for r in x:
        print(r)
    print()

def run_sql(csvs, ex, b = True):
    if (isinstance(csvs, str)):
        conn = sql.connect(f'{csvs}.db')
        x = conn.cursor()
        x.execute(ex.format(csvs))
        print_sql(x, csvs, b)
        conn.close()
    
    elif isinstance(csvs, dict) or isinstance(csvs, set):
        for csv in csvs:
            run_sql(csv, ex, b)
