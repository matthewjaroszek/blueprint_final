import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

csvs = {
    "rc" : "rc.gz",
    "dc" : "dc.gz",
    "trc" : "tdc.gz",
    "tdc" : "tdc.gz",
}

def getdf(csv):
    return pd.read_csv(csvs[csv])

def summarize(csvs, n):
    if isinstance(csvs, str):
        print(f'\n{csvs}: ', end = "")
        summarize(getdf(csvs), n)
    
    elif isinstance(csvs, dict):
        for csv in csvs:
            summarize(csv, n)

    elif isinstance(csvs, pd.DataFrame):
        #print("{:^152}".format(f':{csvs.shape[0]} x {csvs.shape[1]}\n'))
        print(f'{csvs.shape[0]} x {csvs.shape[1]} ', '-'*170, '\n')
        cols = csvs.columns
        x = 0
        for col in cols:
            x += 1
            print(f'{col:^28}', end = "")
            if x >= 6:
                print("")
                x = 0
            else:
                print(" - ", end = "")
        print("\b\b  ")
        if (n > 0):
            print("\n\n", csvs.head(n))