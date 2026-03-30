import pandas as pd

def summary(csv, n):
    print(csv, "\n")
    df = pd.read_csv(csvs[csv])
    cols = df.columns
    for col in cols:
        print(col, " - ", end="")
    print("\n\n", df.head(n))

csvs = {
    "recent_caps.csv" : "GlobalWeatherRepository.csv.gz"
}

for csv in csvs:
    summary(csv, 3)
