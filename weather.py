import pandas as pd

def summary(csv, n):
    print(csv,  "\n")
    df = pd.read_csv(csvs[csv])
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

def summarizeAll(n):
    for csv in csvs:
        summary(csv, n)

csvs = {
    "recentCaps" : "GlobalWeatherRepository.csv.gz",
    "histDC" : "dc_weather.csv.gz"
}

summarizeAll(3)