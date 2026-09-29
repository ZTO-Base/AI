import sqlite3
import pandas as pd


with sqlite3.connect('data/nsmc.db') as conn:
    df = pd.read_sql('SELECT * FROM train_data',conn)
print(df.head())
print(df.info())