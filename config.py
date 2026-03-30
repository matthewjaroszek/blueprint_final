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
        print(f'{csvs}')
        summarize(getdf(csvs), n)
    
    elif isinstance(csvs, dict):
        for csv in csvs:
            summarize(csv, n)

    elif isinstance(csvs, pd.DataFrame):
        print(f'Num rows: {csvs.shape[0]}')
        print(f'Num cols: {csvs.shape[1]}', "\n")
        cols = csvs.columns
        x = 0
        for col in cols:
            x += 1
            print(f'{col:^28}', end = "")
            if x >= 5:
                print("")
                x = 0
            else:
                print(" - ", end = "")
        print("\b\b  \n\n", csvs.head(n))