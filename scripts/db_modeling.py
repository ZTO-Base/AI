import sqlite3
from process_train_test import df, df2

if __name__ == "__main__":
    with sqlite3.connect('data/nsmc.db') as conn:

        df.to_sql('train_data', conn, if_exists='replace', index=False)
        df2.to_sql('test_data', conn, if_exists='replace', index=False)