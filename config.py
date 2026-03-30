import pandas as pd
from dotenv import load_dotenv
import os

csvs = {
    "recent_capital" : "GlobalWeatherRepository.csv.gz",
    "history_DC" : "dc_weather.csv.gz",
    "test" : "test.csv.gz"
}

def getdf(csv):
    return pd.read_csv(csvs[csv])

def summarize(csvs, n):
    if isinstance(csvs, str):
        print(csvs,  "\n")
        df = getdf(csvs)
        print(f'Num rows: {df.shape[0]}')
        print(f'Num cols: {df.shape[1]}', "\n")
        cols = df.columns
        x = 0
        for col in cols:
            x += 1
            print(col, end = "")
            if x >= 5:
                print("\n")
                x = 0
            else:
                print(" - ", end = "")
        print("\b\b  \n\n", df.head(n))
    
    elif isinstance(csvs, dict):
        for csv in csvs:
            summarize(csv, n)