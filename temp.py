from config import *


def nc(csv, old, new):
    df = getdf(csv)
    df = df.rename(columns={old: new})
    df.to_csv(csvs[csv], index = False)

def drop(csv, col):
    df = getdf(csv)
    df = df.drop(col, axis = 1)
    df.to_csv(csvs[csv], index = False)