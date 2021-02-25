import pandas as pd
df = pd.read_csv('milk_2.csv')

monthlyMedian = df['Monthly milk production: pounds per cow'].median()

df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].fillna(value = monthlyMedian)

df['Number of Cows'] = df['Number of Cows'].fillna(method='ffill')

print(df['Monthly milk production: pounds per cow'].mean())
print(df['Monthly milk production: pounds per cow'].std())
print(df['Number of Cows'].mean())
