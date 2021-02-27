import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
regionYearGroup = df.groupby(['region','year']).mean()
regionYearGroup.loc[('Albany',2017)]['AveragePrice']
