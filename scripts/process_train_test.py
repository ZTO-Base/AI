import pandas as pd
 
df = pd.read_csv('data/raw/ratings_train.txt', sep='\t')
df2 = pd.read_csv('data/raw/ratings_test.txt', sep='\t')


def prepare_data(df: pd.DataFrame):
    df = df.dropna(subset=['document','label'])
    df['document'] = df['document'].str.strip()

    df['id'] = df['id'].astype(int)
    df['document'] = df['document'].astype(str)
    df['label'] = df['label'].astype(int)

    df = df.drop_duplicates(subset=['document'], keep=False) # 중복은 라벨에 상관없이 전부 제거

    return df

df = prepare_data(df)
df2 = prepare_data(df2)

