import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
highql_wine = wine_df[(wine_df['quality'] >= 8) & (wine_df['residual sugar'] > 5)]

lowacid_wine = wine_df[((wine_df['quality'] == 7) | (wine_df['quality'] >= 8)) & (wine_df['citric acid'] < 0.4)]
print(lowacid_wine['pH'].count())
print(highql_wine.head())
