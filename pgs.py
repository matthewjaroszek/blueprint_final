from config import *
import psycopg2 as sql

conn = sql.connect(os.getenv("sql_url"))