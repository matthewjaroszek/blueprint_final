from config import *
import psycopg

df = getdf("test")
summarize(df, 2)