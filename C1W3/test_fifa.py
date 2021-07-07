import pandas as pd

df = pd.read_csv('data/fifa.csv')
print(df.columns)
df = df[['Name','Overall']]
print()
print(df.head())