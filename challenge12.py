import pandas as pd
import numpy as np

df = pd.read_csv('avocado.csv', index_col = 0)
conv = df[(df['AveragePrice'] >= 2.0) & (df['type'] == 'conventional')]
orga = df[(df['AveragePrice'] >= 2.0) & (df['type'] == 'organic')]

np.intersect1d(pd.unique(conv['year']), pd.unique(orga['year']))
